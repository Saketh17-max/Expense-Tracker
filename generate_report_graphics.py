import os
import subprocess

out_dir = r"C:\Users\venka\Desktop\college\flutter\report_assets"
os.makedirs(out_dir, exist_ok=True)

# 1. Add Transaction Screen Mockup HTML - Clean border-to-border phone
add_tx_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * { box-sizing: border-box; }
  body {
    margin: 0;
    padding: 0;
    background: transparent;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .phone-frame {
    width: 340px;
    height: 520px;
    background: #ffffff;
    border-radius: 32px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    overflow: hidden;
    border: 5px solid #0f172a;
    display: flex;
    flex-direction: column;
  }
  .app-bar {
    padding: 14px 18px;
    display: flex;
    align-items: center;
    border-bottom: 1px solid #f1f5f9;
  }
  .app-bar h3 {
    margin: 0;
    font-size: 16px;
    font-weight: 700;
    color: #0f172a;
    flex-grow: 1;
    text-align: center;
  }
  .close-btn {
    font-size: 18px;
    color: #64748b;
  }
  .body {
    padding: 20px;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .segmented {
    display: flex;
    background: #f1f5f9;
    padding: 3px;
    border-radius: 10px;
    margin-bottom: 16px;
  }
  .seg-btn {
    flex: 1;
    padding: 8px;
    text-align: center;
    font-size: 13px;
    font-weight: 600;
    border-radius: 8px;
    color: #64748b;
  }
  .seg-btn.active {
    background: #ffffff;
    color: #0f172a;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  }
  .label {
    font-size: 10px;
    font-weight: 700;
    color: #94A3B8;
    letter-spacing: 0.8px;
    margin-bottom: 4px;
  }
  .amount-input {
    font-size: 26px;
    font-weight: 800;
    color: #0f172a;
    display: flex;
    align-items: center;
    gap: 6px;
    margin-bottom: 6px;
  }
  .divider {
    height: 1px;
    background: #e2e8f0;
    margin-bottom: 14px;
  }
  .field-val {
    font-size: 14.5px;
    font-weight: 500;
    color: #0f172a;
    padding: 4px 0;
    margin-bottom: 4px;
  }
  .save-btn {
    background: #0f172a;
    color: white;
    text-align: center;
    padding: 13px;
    border-radius: 12px;
    font-weight: 700;
    font-size: 14px;
    margin-top: 10px;
  }
</style>
</head>
<body>
<div class="phone-frame">
  <div class="app-bar">
    <span class="close-btn">&#10005;</span>
    <h3>New Transaction</h3>
    <span style="width:18px;"></span>
  </div>
  <div class="body">
    <div>
      <div class="segmented">
        <div class="seg-btn">Income</div>
        <div class="seg-btn active">Expense</div>
      </div>
      
      <div class="label">AMOUNT</div>
      <div class="amount-input">
        <span style="color:#0f172a;">₹</span>
        <span>1,450.00</span>
      </div>
      <div class="divider"></div>
      
      <div class="label">TITLE</div>
      <div class="field-val">Raw Material Inventory</div>
      <div class="divider"></div>
      
      <div class="label">CATEGORY</div>
      <div class="field-val" style="display:flex; justify-content:space-between; align-items:center;">
        <span>Supplies</span>
        <span style="color:#94a3b8; font-size:11px;">&#9660;</span>
      </div>
      <div class="divider"></div>
      
      <div class="label">DATE</div>
      <div class="field-val" style="display:flex; justify-content:space-between; align-items:center;">
        <span>04 Nov 2026</span>
        <span style="color:#94a3b8; font-size:15px;">&#128197;</span>
      </div>
      <div class="divider"></div>
    </div>
    
    <div class="save-btn">Save Transaction</div>
  </div>
</div>
</body>
</html>
"""

# 2. Delete Confirmation Dialog Mockup HTML - Clean border-to-border phone
delete_dialog_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * { box-sizing: border-box; }
  body {
    margin: 0;
    padding: 0;
    background: transparent;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .phone-frame {
    width: 340px;
    height: 520px;
    background: #334155;
    border-radius: 32px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    overflow: hidden;
    border: 5px solid #0f172a;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 18px;
  }
  .dialog-card {
    background: #ffffff;
    border-radius: 20px;
    padding: 22px;
    width: 100%;
    box-shadow: 0 15px 25px rgba(0,0,0,0.25);
  }
  .dialog-title {
    font-size: 17px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 8px;
  }
  .dialog-desc {
    font-size: 13px;
    color: #64748b;
    line-height: 1.45;
    margin-bottom: 20px;
  }
  .actions {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
  }
  .btn-cancel {
    padding: 8px 16px;
    border-radius: 10px;
    font-size: 13px;
    font-weight: 600;
    color: #64748b;
    background: #f1f5f9;
  }
  .btn-delete {
    background: #ef4444;
    color: white;
    padding: 8px 18px;
    border-radius: 10px;
    font-size: 13px;
    font-weight: 600;
  }
</style>
</head>
<body>
<div class="phone-frame">
  <div class="dialog-card">
    <div class="dialog-title">Delete Transaction?</div>
    <div class="dialog-desc">Are you sure you want to delete this transaction from your business records? This updates your balance immediately.</div>
    <div class="actions">
      <div class="btn-cancel">Cancel</div>
      <div class="btn-delete">Delete</div>
    </div>
  </div>
</div>
</body>
</html>
"""

with open(os.path.join(out_dir, "add_tx.html"), "w", encoding="utf-8") as f:
    f.write(add_tx_html)

with open(os.path.join(out_dir, "dialog.html"), "w", encoding="utf-8") as f:
    f.write(delete_dialog_html)

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

subprocess.run([
    chrome, "--headless=new", "--disable-gpu", "--no-sandbox",
    "--window-size=350,530",
    f"--screenshot={os.path.join(out_dir, 'add_transaction_screen.png')}",
    os.path.join(out_dir, "add_tx.html")
])

subprocess.run([
    chrome, "--headless=new", "--disable-gpu", "--no-sandbox",
    "--window-size=350,530",
    f"--screenshot={os.path.join(out_dir, 'delete_dialog_screen.png')}",
    os.path.join(out_dir, "dialog.html")
])

print("Regenerated clean border-to-border mobile mockups!")
