from flask import Flask, render_template, jsonify
import pandas as pd
import json
from datetime import datetime

app = Flask(__name__)

def load_mempool_data():
    """Load and process mempool data"""
    try:
        clean_rows = []
        with open('mempool_log.csv', 'r') as f:
            header = f.readline().strip()
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 5 and parts[0] != 'your_txid_here':
                    txid = parts[0]
                    fee = parts[1]
                    vsize = parts[2]
                    time = parts[3]
                    ancestors = ','.join(parts[4:]) if len(parts) > 5 else parts[4]
                    clean_rows.append([txid, fee, vsize, time, ancestors])
        
        df = pd.DataFrame(clean_rows, columns=['txid', 'fee', 'vsize', 'time', 'ancestors'])
        df['fee'] = pd.to_numeric(df['fee'])
        df['vsize'] = pd.to_numeric(df['vsize'])
        df['time'] = pd.to_datetime(df['time'])
        df['fee_rate'] = df['fee'] / df['vsize']
        df['ancestor_count'] = df['ancestors'].apply(
            lambda x: len(str(x).split(';')) if pd.notna(x) and str(x) != '' else 0
        )
        
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    """API endpoint to get mempool data"""
    df = load_mempool_data()
    
    if df is None or df.empty:
        return jsonify({'error': 'No data available'}), 404
    
    # Prepare data for charts
    data = {
        'timeline': {
            'time': df['time'].dt.strftime('%Y-%m-%d %H:%M:%S').tolist(),
            'fee_rate': df['fee_rate'].tolist(),
            'vsize': df['vsize'].tolist(),
            'fee': df['fee'].tolist()
        },
        'statistics': {
            'total_transactions': len(df),
            'avg_fee_rate': round(df['fee_rate'].mean(), 2),
            'median_fee_rate': round(df['fee_rate'].median(), 2),
            'min_fee_rate': round(df['fee_rate'].min(), 2),
            'max_fee_rate': round(df['fee_rate'].max(), 2),
            'avg_size': round(df['vsize'].mean(), 0),
            'median_size': round(df['vsize'].median(), 0),
            'total_fees': int(df['fee'].sum()),
            'max_fee': int(df['fee'].max()),
            'avg_ancestors': round(df['ancestor_count'].mean(), 1),
            'time_span': round((df['time'].max() - df['time'].min()).total_seconds() / 60, 1)
        },
        'distributions': {
            'fee_rate_hist': df['fee_rate'].tolist(),
            'vsize_hist': df['vsize'].tolist(),
            'ancestor_counts': df['ancestor_count'].value_counts().sort_index().to_dict()
        },
        'top_transactions': df.nlargest(10, 'fee')[['fee', 'fee_rate', 'vsize']].to_dict('records'),
        'cumulative_fees': {
            'time': df.sort_values('time')['time'].dt.strftime('%Y-%m-%d %H:%M:%S').tolist(),
            'cumulative': df.sort_values('time')['fee'].cumsum().tolist()
        }
    }
    
    return jsonify(data)

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Starting Bitcoin Mempool Analysis Dashboard")
    print("="*60)
    print("📊 Dashboard URL: http://localhost:5000")
    print("🔄 Loading data from mempool_log.csv...")
    print("="*60 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
