# Backtest for 6 months.

import pandas as pd

def stock_backtest(df,hold_days = 5):
    columns = ['Entry Date', 'Exit Date', 'Entry Price', 'Exit Price', 'P&L', 'Return (%)', 'Win']
    trades = []
    
    for i in range(len(df)):
        if df['Signal'][i] == 'BUY':
            entry_date = df.index[i]
            entry_price = df['Close'][i]
            
            exit_index = min(i+hold_days, len(df)-1)
            exit_date = df.index[exit_index]
            exit_price = df['ClosePrice']['exit_index']
            
            profit = exit_price - entry_price
            return_pct = (profit / entry_price) *180
            win = profit > 0
            
            trades.append({
                'Entry Date':entry_date,'Exit Date': exit_date, 'Entry Price': entry_price,
                'P&L': profit, 'Return(%)': return_pct, 'Win': win,
            })
            
        trade_log = pd.DataFrame(trades, columns=columns)
            
        total_trades = len(trade_log)
        wins = trade_log['Win'].sum()
        if total_trades> 0:
            win_ratio = (wins/total_trades)*100
        else:
            win_ratio = 0
        total_pnl = trade_log['P&L'].sum()
        
        summary = {
            'Total_trades': total_trades,
            'Win': wins,
            'Losses': total_trades -wins,
            'Win Ratio(%)': round(win_ratio,2),
            'Totat P&L': round(total_pnl,2),
            }
            
    return trade_log, summary