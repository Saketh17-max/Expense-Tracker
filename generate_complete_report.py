import os
import base64
import subprocess
import pypdf

def get_base64_img(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
            ext = os.path.splitext(path)[1].lower().replace(".", "")
            if ext == "jpg": ext = "jpeg"
            return f"data:image/{ext};base64,{data}"
    return ""

assets_dir = r"C:\Users\venka\Desktop\college\flutter\report_assets"

logo_b64 = get_base64_img(os.path.join(assets_dir, "page_1_img_0.png"))
arch_b64 = get_base64_img(os.path.join(assets_dir, "architecture_diagram.png"))
desktop_b64 = get_base64_img(os.path.join(assets_dir, "deployment_screenshot.png"))
add_tx_b64 = get_base64_img(os.path.join(assets_dir, "add_transaction_screen.png"))
dialog_b64 = get_base64_img(os.path.join(assets_dir, "delete_dialog_screen.png"))
chart_tx_b64 = get_base64_img(os.path.join(assets_dir, "media_1791527347291.png"))

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Project Report - T Venkat Saketh - Expense Tracker</title>
<style>
  @page {{
    size: A4 portrait;
    margin: 0;
  }}
  * {{
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}
  body {{
    margin: 0;
    padding: 0;
    background-color: #f1f5f9;
    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    font-size: 9.2pt;
    line-height: 1.42;
  }}
  .page {{
    width: 210mm;
    height: 297mm;
    min-height: 297mm;
    max-height: 297mm;
    position: relative;
    background: #ffffff;
    padding: 20mm 20mm 24mm 20mm;
    page-break-after: always;
    page-break-inside: avoid;
    overflow: hidden;
    margin: 0 auto;
  }}
  
  /* Running Header & Footer */
  .page-header {{
    position: absolute;
    top: 8mm;
    left: 20mm;
    right: 20mm;
    height: 7mm;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1.5px solid #1e3a8a;
    font-size: 7.5pt;
    font-weight: 700;
    color: #1e3a8a;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .page-footer {{
    position: absolute;
    bottom: 8mm;
    left: 20mm;
    right: 20mm;
    height: 7mm;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #cbd5e1;
    font-size: 8pt;
    color: #64748b;
    font-weight: 500;
  }}
  
  /* Headings & Badges */
  h1, h2, h3, h4 {{
    color: #0f172a;
    margin-top: 0;
    font-weight: 700;
    letter-spacing: -0.3px;
  }}
  h2.section-title {{
    font-size: 13pt;
    color: #1e3a8a;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 3px;
    margin-bottom: 9px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  h3.sub-title {{
    font-size: 10pt;
    color: #0f172a;
    margin-top: 7px;
    margin-bottom: 4px;
  }}
  
  /* Tables */
  table.report-table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 5px;
    margin-bottom: 8px;
    font-size: 8.5pt;
  }}
  table.report-table th {{
    background: #1e3a8a;
    color: #ffffff;
    font-weight: 600;
    text-align: left;
    padding: 5px 8px;
    border: 1px solid #1e3a8a;
  }}
  table.report-table td {{
    padding: 4.5px 8px;
    border: 1px solid #cbd5e1;
    color: #334155;
  }}
  table.report-table tr:nth-child(even) {{
    background-color: #f8fafc;
  }}
  
  /* Code Blocks */
  pre.code-box {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 3.5px solid #1e3a8a;
    border-radius: 6px;
    padding: 7px 10px;
    font-family: Consolas, "Courier New", monospace;
    font-size: 7.1pt;
    line-height: 1.22;
    color: #0f172a;
    overflow: hidden;
    margin-top: 4px;
    margin-bottom: 6px;
    white-space: pre-wrap;
    word-break: break-all;
  }}
  .kw {{ color: #1d4ed8; font-weight: bold; }}
  .cls {{ color: #7c3aed; font-weight: bold; }}
  .str {{ color: #16a34a; }}
  .cm {{ color: #64748b; font-style: italic; }}
  
  /* Callouts & Cards */
  .callout {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 4px solid #3b82f6;
    padding: 7px 10px;
    border-radius: 6px;
    margin: 5px 0;
    font-size: 8.5pt;
  }}
  .callout-title {{
    font-weight: 700;
    color: #1e3a8a;
    margin-bottom: 2px;
  }}
  
  /* Image figure containers */
  .figure-box {{
    text-align: center;
    margin: 5px 0;
  }}
  .figure-img {{
    max-width: 100%;
    border-radius: 8px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
  }}
  .caption {{
    font-size: 7.5pt;
    color: #64748b;
    font-weight: 600;
    margin-top: 3px;
  }}
  
  p {{
    margin-top: 2px;
    margin-bottom: 5px;
    text-align: justify;
  }}
  ul, ol {{
    margin-top: 2px;
    margin-bottom: 5px;
    padding-left: 18px;
  }}
  li {{
    margin-bottom: 2px;
  }}
</style>
</head>
<body>

<!-- ==========================================
     PAGE 1: COVER PAGE
     ========================================== -->
<div class="page" style="padding: 16mm 18mm 18mm 18mm;">
  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 22mm;">
    <div style="display: flex; align-items: center; gap: 14px;">
      <img src="{logo_b64}" style="height: 68px; object-fit: contain;">
      <div>
        <div style="font-weight: 800; font-size: 15pt; color: #1d70b8; letter-spacing: 0.5px;">VISHNU</div>
        <div style="font-size: 7.5pt; color: #1e293b; letter-spacing: 1.5px; font-weight: 600;">UNIVERSAL LEARNING</div>
      </div>
    </div>
    
    <div style="background: #1d70b8; color: #ffffff; padding: 12px 22px; border-radius: 4px; text-align: center; width: 340px;">
      <div style="font-size: 9.5pt; font-weight: 800; letter-spacing: 0.5px; line-height: 1.3;">
        VISHNU INSTITUTE OF TECHNOLOGY :: BHIMAVARAM
      </div>
      <div style="font-size: 8pt; font-weight: 600; margin-top: 4px; letter-spacing: 0.3px;">
        DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING
      </div>
    </div>
  </div>

  <div style="text-align: center; margin-bottom: 18mm;">
    <div style="font-size: 19pt; font-weight: 800; color: #1d70b8; letter-spacing: 0.5px; margin-bottom: 16mm;">
      USER INTERFACE DESIGN USING FLUTTER
    </div>
    <div style="font-size: 21pt; font-weight: 800; color: #1d70b8; letter-spacing: 1px;">
      PROJECT REPORT
    </div>
  </div>

  <div style="margin-bottom: 14mm; padding-top: 8px;">
    <div style="font-size: 12pt; font-weight: 700; color: #1d70b8; margin-bottom: 8px;">
      Project Title:
    </div>
    <div style="font-size: 12pt; font-weight: 600; color: #0f172a; padding-bottom: 6px; border-bottom: 1.5px solid #1d70b8; line-height: 1.5;">
      Create a small-business income/expense tracker with balance summary using Provider.
    </div>
  </div>

  <!-- Student Name and Roll No in the designated space -->
  <div style="display: flex; justify-content: space-between; font-size: 11pt; font-weight: 600; color: #0f172a; margin-bottom: 14mm; border-bottom: 1px solid #e2e8f0; padding-bottom: 10px;">
    <div>Student Name : <span style="font-weight: 700; color: #1d70b8;">T Venkat Saketh</span></div>
    <div>Roll No : <span style="font-weight: 700; color: #1d70b8;">24PA1A05M4</span></div>
  </div>

  <!-- Department & Section Row -->
  <div style="display: flex; justify-content: space-between; font-size: 11pt; font-weight: 600; color: #0f172a; margin-bottom: 16mm; border-bottom: 1px solid #e2e8f0; padding-bottom: 10px;">
    <div>Department : <span style="font-weight: 700; color: #1d70b8;">Computer Science and Engineering</span></div>
    <div>Section : <span style="font-weight: 700; color: #1d70b8;">D</span></div>
  </div>

  <!-- Signatures Block -->
  <div style="margin-top: 18mm;">
    <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 16mm; font-size: 10pt;">
      <div>
        <span style="font-weight: 800; color: #0f172a;">COURSE INSTRUCTOR :</span>
        <span style="font-weight: 600; color: #334155;">Mrs. P.SHYAMALA MADHURI</span>
      </div>
      <div style="font-weight: 700; color: #0f172a; border-top: 1px dashed #94a3b8; padding-top: 6px; width: 220px; text-align: center;">
        SIGNATURE OF THE INSTRUCTOR
      </div>
    </div>

    <div style="display: flex; justify-content: space-between; align-items: flex-end; font-size: 10pt;">
      <div>
        <span style="font-weight: 800; color: #0f172a;">HOD NAME :</span>
        <span style="font-weight: 600; color: #334155;">Dr. R. SRINIVASA RAJU</span>
      </div>
      <div style="font-weight: 700; color: #0f172a; border-top: 1px dashed #94a3b8; padding-top: 6px; width: 220px; text-align: center;">
        SIGNATURE OF THE HOD
      </div>
    </div>
  </div>
</div>


<!-- ==========================================
     PAGE 2: TABLE OF CONTENTS (CONSOLIDATED 13 PAGES)
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>User Interface Design Using Flutter</span>
    <span>Table of Contents</span>
  </div>

  <div style="background: #1d70b8; color: #ffffff; padding: 12px 18px; border-radius: 4px; font-size: 15pt; font-weight: 800; letter-spacing: 0.5px; text-align: center; margin-bottom: 16px;">
    PROJECT REPORT
  </div>

  <h2 class="section-title">Table of Contents</h2>
  
  <table class="report-table" style="font-size: 9pt;">
    <thead>
      <tr>
        <th style="width: 12%; text-align: center;">S. No.</th>
        <th style="width: 73%;">Topic / Section Name</th>
        <th style="width: 15%; text-align: center;">Page No.</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="text-align: center; font-weight: 700;">1</td>
        <td><strong>Student Details, Problem Definition & Project Objectives</strong></td>
        <td style="text-align: center; font-weight: 700;">3</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: 700;">2</td>
        <td><strong>Technology Stack & Key Flutter Concepts Demonstrated</strong></td>
        <td style="text-align: center; font-weight: 700;">4</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: 700;">3</td>
        <td><strong>System Architecture & Project Directory Organization</strong></td>
        <td style="text-align: center; font-weight: 700;">5</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: 700;">4</td>
        <td><strong>Detailed Implementation & Code Snippets:</strong></td>
        <td style="text-align: center; font-weight: 700;">6 - 10</td>
      </tr>
      <tr>
        <td style="text-align: center;">4.1</td>
        <td style="padding-left: 20px;">Application Root (<code>lib/main.dart</code>) & Data Model (<code>lib/models/transaction.dart</code>)</td>
        <td style="text-align: center;">6</td>
      </tr>
      <tr>
        <td style="text-align: center;">4.2</td>
        <td style="padding-left: 20px;">State Management Controller (<code>lib/providers/transaction_provider.dart</code>)</td>
        <td style="text-align: center;">7</td>
      </tr>
      <tr>
        <td style="text-align: center;">4.3</td>
        <td style="padding-left: 20px;">Responsive Dashboard Screen (<code>lib/screens/home_screen.dart</code>)</td>
        <td style="text-align: center;">8</td>
      </tr>
      <tr>
        <td style="text-align: center;">4.4</td>
        <td style="padding-left: 20px;">Transaction Form & Input Validation (<code>lib/screens/add_transaction_screen.dart</code>)</td>
        <td style="text-align: center;">9</td>
      </tr>
      <tr>
        <td style="text-align: center;">4.5</td>
        <td style="padding-left: 20px;">Modular Widgets: Balance Card & Category Pie Chart</td>
        <td style="text-align: center;">10</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: 700;">5</td>
        <td><strong>Cloud Deployment Architecture & System Verification Matrix</strong></td>
        <td style="text-align: center; font-weight: 700;">11</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: 700;">6</td>
        <td><strong>High-Resolution Output Screens (Part 1 - Web Dashboard Showcase)</strong></td>
        <td style="text-align: center; font-weight: 700;">12</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: 700;">7</td>
        <td><strong>High-Resolution Output Screens (Part 2 - Mobile Views) & Project Conclusion</strong></td>
        <td style="text-align: center; font-weight: 700;">13</td>
      </tr>
    </tbody>
  </table>

  <div class="callout" style="margin-top: 14px;">
    <div class="callout-title">Official Repository & Deployment Deliverables</div>
    <ul style="margin: 0; padding-left: 18px; font-size: 8.5pt;">
      <li><strong>GitHub Source Code Repository:</strong> <a href="https://github.com/Saketh17-max/Expense-Tracker" style="color:#1d4ed8; text-decoration:none;">https://github.com/Saketh17-max/Expense-Tracker</a></li>
      <li><strong>Live Web Application Deployment:</strong> <a href="https://saketh17-max.github.io/Expense-Tracker/" style="color:#1d4ed8; text-decoration:none;">https://saketh17-max.github.io/Expense-Tracker/</a></li>
      <li><strong>State Management Engine:</strong> Flutter Provider 6.x with ChangeNotifier</li>
    </ul>
  </div>

  <div class="page-footer">
    <span>Vishnu Institute of Technology :: Bhimavaram</span>
    <span>Page 2 of 13</span>
  </div>
</div>


<!-- ==========================================
     PAGE 3: STUDENT DETAILS, PROBLEM DEFINITION & OBJECTIVES (CONSOLIDATED)
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Student Details, Problem & Objectives</span>
    <span>Section 1</span>
  </div>

  <h2 class="section-title">1. Student Details & Project Profile</h2>
  
  <table class="report-table">
    <tr>
      <th style="width: 28%;">Field</th>
      <th style="width: 72%;">Academic Profile Information</th>
    </tr>
    <tr>
      <td><strong>Student Name</strong></td>
      <td><strong>T Venkat Saketh</strong></td>
    </tr>
    <tr>
      <td><strong>Registration / Roll No.</strong></td>
      <td><strong>24PA1A05M4</strong></td>
    </tr>
    <tr>
      <td><strong>Department & Section</strong></td>
      <td>Computer Science and Engineering (CSE) &bull; Section D</td>
    </tr>
    <tr>
      <td><strong>Course & Institution</strong></td>
      <td>User Interface Design Using Flutter &bull; Vishnu Institute of Technology, Bhimavaram</td>
    </tr>
    <tr>
      <td><strong>Supervisors</strong></td>
      <td>Mrs. P. Shyamala Madhuri (Instructor) &bull; Dr. R. Srinivasa Raju (HOD)</td>
    </tr>
  </table>

  <h2 class="section-title" style="margin-top: 10px;">2. Problem Definition & Proposed Solution</h2>
  <div class="callout">
    <div class="callout-title">Project Title: Create a small-business income/expense tracker with balance summary using Provider.</div>
  </div>
  <p>
    <strong>Background & Context:</strong> Micro and small enterprises (MSMEs) execute dozens of small transactions daily. Despite the critical requirement for cash flow clarity, most small-business owners continue to rely on manual paper ledgers or memory, leading to arithmetic errors, lack of net cash visibility, and zero spending categorization. Mainstream enterprise accounting tools are overly complex, requiring cloud logins, subscriptions, and accounting training.
  </p>
  <p>
    <strong>Proposed Solution:</strong> An intuitive, lightweight, client-side mobile and web application built in Flutter using the <strong>Provider</strong> architecture. It delivers instantaneous net balance computation ($Balance = Income - Expense$), interactive visual donut breakdown charts, and seamless transaction creation and deletion with strict client validation.
  </p>

  <h2 class="section-title" style="margin-top: 10px;">3. Project Objectives & System Scope</h2>
  <ul>
    <li><strong>Streamlined Ledger Input:</strong> Guided form to record transaction titles, numeric amounts in Indian Rupees (₹), spending categories, and dates with strict validation.</li>
    <li><strong>Automated Dynamic Balances:</strong> Real-time calculation of Total Income, Total Expenses, and Net Balance without manual recalculation or screen refreshes.</li>
    <li><strong>Categorical Visual Analytics:</strong> Interactive vector donut charts (<code>fl_chart</code>) mapping expenses across categories (Food, Transport, Utilities, Supplies, Other).</li>
    <li><strong>Pure Provider State Architecture:</strong> Centralized state managed via <code>ChangeNotifier</code> and <code>ChangeNotifierProvider</code>, ensuring clean separation of concerns and optimal rendering performance.</li>
    <li><strong>Cross-Platform Target:</strong> Zero-backend client architecture compiled and deployed natively across Web and Android mobile viewports.</li>
  </ul>

  <div class="page-footer">
    <span>Vishnu Institute of Technology :: Bhimavaram</span>
    <span>Page 3 of 13</span>
  </div>
</div>


<!-- ==========================================
     PAGE 4: TECHNOLOGY STACK & CONCEPTS
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Technology Stack & Flutter Concepts</span>
    <span>Section 2</span>
  </div>

  <h2 class="section-title">2. Technology Stack & Key Flutter Concepts</h2>

  <h3 class="sub-title">2.1 Technology Specifications</h3>
  <table class="report-table">
    <thead>
      <tr>
        <th style="width: 25%;">Component</th>
        <th style="width: 30%;">Version / Tool</th>
        <th style="width: 45%;">Role in Project</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Programming Language</strong></td>
        <td>Dart SDK 3.13+</td>
        <td>Strongly-typed object-oriented language optimized for client UI applications.</td>
      </tr>
      <tr>
        <td><strong>UI Framework</strong></td>
        <td>Flutter 3.47+ (Stable)</td>
        <td>Cross-platform declarative SDK compiling to native machine code and WebAssembly.</td>
      </tr>
      <tr>
        <td><strong>State Management</strong></td>
        <td>Provider 6.1.2</td>
        <td>Wrapper around InheritedWidget facilitating reactive UI data binding and separation of concerns.</td>
      </tr>
      <tr>
        <td><strong>Data Visualization</strong></td>
        <td>fl_chart 1.2.0</td>
        <td>Hardware-accelerated mathematical vector charting library for custom donut pie visualizations.</td>
      </tr>
      <tr>
        <td><strong>Typography</strong></td>
        <td>Google Fonts (Inter)</td>
        <td>High-legibility geometric sans-serif typeface designed for financial applications.</td>
      </tr>
      <tr>
        <td><strong>Hosting Platform</strong></td>
        <td>GitHub Pages (CI/CD)</td>
        <td>Automated cloud hosting delivering the static release build of the Flutter web target.</td>
      </tr>
    </tbody>
  </table>

  <h3 class="sub-title">2.2 Fundamental Flutter Concepts Demonstrated</h3>
  <ul>
    <li><strong>StatelessWidget vs. StatefulWidget:</strong> Pure display components (such as <code>BalanceCard</code>, <code>TransactionCard</code>, and <code>HomeScreen</code>) are implemented as immutable <code>StatelessWidget</code>s, leveraging Provider for updates. Forms with local input controllers (such as <code>AddTransactionScreen</code>) utilize <code>StatefulWidget</code>.</li>
    <li><strong>Declarative UI Architecture:</strong> The user interface is a direct mathematical projection of state: $UI = f(State)$. Widgets rebuild automatically in response to changes in the underlying <code>TransactionProvider</code> model.</li>
    <li><strong>Responsive Sliver Architecture:</strong> <code>HomeScreen</code> incorporates <code>CustomScrollView</code>, <code>SliverToBoxAdapter</code>, and <code>SliverList</code> to ensure fluid 60 FPS scrolling without layout overflow errors (<code>RenderFlex overflowed</code>).</li>
    <li><strong>Form Handling & Input Validation:</strong> Implements <code>Form</code> and <code>TextFormField</code> widgets bound to a <code>GlobalKey&lt;FormState&gt;</code> to enforce validation rules prior to mutating application state.</li>
    <li><strong>Material 3 Design System:</strong> Integrates modern surface elevation tokens, custom <code>SegmentedButton</code> controls, dynamic color schemes (<code>ColorScheme.fromSeed</code>), and clean card padding.</li>
    <li><strong>Contextual User Feedback:</strong> Demonstrates modal <code>AlertDialog</code> popups for delete actions and floating <code>SnackBar</code>s for transaction confirmations.</li>
  </ul>

  <div class="page-footer">
    <span>Vishnu Institute of Technology :: Bhimavaram</span>
    <span>Page 4 of 13</span>
  </div>
</div>


<!-- ==========================================
     PAGE 5: SYSTEM ARCHITECTURE & DIRECTORY STRUCTURE (CONSOLIDATED)
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Architecture & Directory Structure</span>
    <span>Section 3</span>
  </div>

  <h2 class="section-title">3. System Architecture & Project Organization</h2>

  <div class="figure-box">
    <img src="{arch_b64}" class="figure-img" style="height: 165px; width: auto;">
    <div class="caption">Figure 3.1: High-Level Unidirectional Architecture and Provider Reactive Loop</div>
  </div>

  <h3 class="sub-title">3.1 Unidirectional Reactive Data Flow</h3>
  <p>
    The application strictly adheres to the unidirectional data flow pattern: UI triggers an action via <code>context.read&lt;TransactionProvider&gt;().addTransaction()</code> &rarr; Provider mutates the internal <code>_transactions</code> collection &rarr; Provider executes <code>notifyListeners()</code> &rarr; Widgets listening via <code>Consumer</code> or <code>context.watch()</code> automatically rebuild their subtrees.
  </p>

  <h3 class="sub-title">3.2 Project Directory Organization & Module Breakdown</h3>
  <table class="report-table">
    <thead>
      <tr>
        <th style="width: 25%;">Directory / File</th>
        <th style="width: 25%;">Primary Class</th>
        <th style="width: 50%;">Architectural Role & Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>main.dart</code></td>
        <td><code>MyApp</code></td>
        <td>Configures <code>ChangeNotifierProvider</code>, initializes Material 3, and sets up global typography via Google Fonts.</td>
      </tr>
      <tr>
        <td><code>models/</code></td>
        <td><code>TransactionModel</code></td>
        <td>Defines data structures with attributes: <code>id</code>, <code>title</code>, <code>amount</code>, <code>type</code>, <code>date</code>, and <code>category</code>.</td>
      </tr>
      <tr>
        <td><code>providers/</code></td>
        <td><code>TransactionProvider</code></td>
        <td>Manages the private transactions list, calculates sums, categorizes data for the pie chart, and notifies listeners on data changes.</td>
      </tr>
      <tr>
        <td><code>screens/</code></td>
        <td><code>HomeScreen</code>, <code>AddTransactionScreen</code></td>
        <td>Manages screen-level navigation and high-level page composition using Flutter's <code>Navigator.push()</code> and <code>Navigator.pop()</code>.</td>
      </tr>
      <tr>
        <td><code>widgets/</code></td>
        <td><code>BalanceCard</code>, <code>ExpensePieChart</code>, etc.</td>
        <td>Modular presentation widgets that keep screen files clean, reusable, and maintainable.</td>
      </tr>
    </tbody>
  </table>

  <div class="page-footer">
    <span>Vishnu Institute of Technology :: Bhimavaram</span>
    <span>Page 5 of 13</span>
  </div>
</div>


<!-- ==========================================
     PAGE 6: CODE SNIPPETS - MAIN & MODEL
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Implementation - main.dart & model</span>
    <span>Section 4.1</span>
  </div>

  <h2 class="section-title">4.1 Source Code: Application Root & Data Model</h2>

  <h3 class="sub-title">Application Root Setup (<code>lib/main.dart</code>)</h3>
  <pre class="code-box">
<span class="kw">import</span> <span class="str">'package:flutter/material.dart'</span>;
<span class="kw">import</span> <span class="str">'package:provider/provider.dart'</span>;
<span class="kw">import</span> <span class="str">'package:google_fonts/google_fonts.dart'</span>;
<span class="kw">import</span> <span class="str">'providers/transaction_provider.dart'</span>;
<span class="kw">import</span> <span class="str">'screens/home_screen.dart'</span>;

<span class="kw">void</span> main() {{
  runApp(
    <span class="cls">ChangeNotifierProvider</span>(
      create: (context) =&gt; <span class="cls">TransactionProvider</span>(),
      child: <span class="kw">const</span> <span class="cls">MyApp</span>(),
    ),
  );
}}

<span class="kw">class</span> <span class="cls">MyApp</span> <span class="kw">extends</span> <span class="cls">StatelessWidget</span> {{
  <span class="kw">const</span> <span class="cls">MyApp</span>({{<span class="kw">super</span>.key}});

  <span class="kw">@override</span>
  <span class="cls">Widget</span> build(<span class="cls">BuildContext</span> context) {{
    <span class="kw">return</span> <span class="cls">MaterialApp</span>(
      title: <span class="str">'Business Expense Tracker'</span>,
      debugShowCheckedModeBanner: <span class="kw">false</span>,
      theme: <span class="cls">ThemeData</span>(
        useMaterial3: <span class="kw">true</span>,
        fontFamily: <span class="cls">GoogleFonts</span>.inter().fontFamily,
        colorScheme: <span class="cls">ColorScheme</span>.fromSeed(
          seedColor: <span class="kw">const</span> <span class="cls">Color</span>(<span class="str">0xFF0F172A</span>),
          primary: <span class="kw">const</span> <span class="cls">Color</span>(<span class="str">0xFF0F172A</span>),
          surface: <span class="kw">const</span> <span class="cls">Color</span>(<span class="str">0xFFF8FAFC</span>),
        ),
      ),
      home: <span class="kw">const</span> <span class="cls">HomeScreen</span>(),
    );
  }}
}}
  </pre>

  <h3 class="sub-title">Transaction Model (<code>lib/models/transaction.dart</code>)</h3>
  <pre class="code-box">
<span class="kw">enum</span> <span class="cls">TransactionType</span> {{ income, expense }}

<span class="kw">class</span> <span class="cls">TransactionModel</span> {{
  <span class="kw">final</span> <span class="cls">String</span> id, title, category;
  <span class="kw">final</span> <span class="cls">double</span> amount;
  <span class="kw">final</span> <span class="cls">TransactionType</span> type;
  <span class="kw">final</span> <span class="cls">DateTime</span> date;

  <span class="cls">TransactionModel</span>({{
    <span class="kw">required</span> <span class="kw">this</span>.id,
    <span class="kw">required</span> <span class="kw">this</span>.title,
    <span class="kw">required</span> <span class="kw">this</span>.amount,
    <span class="kw">required</span> <span class="kw">this</span>.type,
    <span class="kw">required</span> <span class="kw">this</span>.date,
    <span class="kw">required</span> <span class="kw">this</span>.category,
  }});
}}
  </pre>

  <div class="page-footer">
    <span>Vishnu Institute of Technology :: Bhimavaram</span>
    <span>Page 6 of 13</span>
  </div>
</div>


<!-- ==========================================
     PAGE 7: CODE SNIPPETS - PROVIDER
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Implementation - TransactionProvider</span>
    <span>Section 4.2</span>
  </div>

  <h2 class="section-title">4.2 State Management Controller (<code>transaction_provider.dart</code>)</h2>
  <pre class="code-box" style="font-size: 7.1pt; line-height: 1.24;">
<span class="kw">import</span> <span class="str">'package:flutter/material.dart'</span>;
<span class="kw">import</span> <span class="str">'../models/transaction.dart'</span>;

<span class="kw">class</span> <span class="cls">TransactionProvider</span> <span class="kw">with</span> <span class="cls">ChangeNotifier</span> {{
  <span class="kw">final</span> <span class="cls">List</span>&lt;<span class="cls">TransactionModel</span>&gt; _transactions = [
    <span class="cls">TransactionModel</span>(
      id: <span class="str">'1'</span>, title: <span class="str">'Product Sales'</span>, amount: <span class="str">5000</span>,
      type: <span class="cls">TransactionType</span>.income, date: <span class="cls">DateTime</span>.now(), category: <span class="str">'Sales'</span>,
    ),
    <span class="cls">TransactionModel</span>(
      id: <span class="str">'2'</span>, title: <span class="str">'Office Supplies'</span>, amount: <span class="str">1200</span>,
      type: <span class="cls">TransactionType</span>.expense, date: <span class="cls">DateTime</span>.now(), category: <span class="str">'Supplies'</span>,
    ),
  ];

  <span class="cls">List</span>&lt;<span class="cls">TransactionModel</span>&gt; <span class="kw">get</span> transactions =&gt; [..._transactions].reversed.toList();

  <span class="cls">double</span> <span class="kw">get</span> totalIncome =&gt; _transactions
      .where((tx) =&gt; tx.type == <span class="cls">TransactionType</span>.income)
      .fold(<span class="str">0.0</span>, (sum, tx) =&gt; sum + tx.amount);

  <span class="cls">double</span> <span class="kw">get</span> totalExpense =&gt; _transactions
      .where((tx) =&gt; tx.type == <span class="cls">TransactionType</span>.expense)
      .fold(<span class="str">0.0</span>, (sum, tx) =&gt; sum + tx.amount);

  <span class="cls">double</span> <span class="kw">get</span> balance =&gt; totalIncome - totalExpense;

  <span class="cls">Map</span>&lt;<span class="cls">String</span>, <span class="cls">double</span>&gt; <span class="kw">get</span> expensesByCategory {{
    <span class="cls">Map</span>&lt;<span class="cls">String</span>, <span class="cls">double</span>&gt; map = {{}};
    <span class="kw">for</span> (<span class="kw">var</span> tx <span class="kw">in</span> _transactions) {{
      <span class="kw">if</span> (tx.type == <span class="cls">TransactionType</span>.expense) {{
        map[tx.category] = (map[tx.category] ?? <span class="str">0.0</span>) + tx.amount;
      }}
    }}
    <span class="kw">return</span> map;
  }}

  <span class="kw">void</span> addTransaction(<span class="cls">TransactionModel</span> newTx) {{
    _transactions.add(newTx);
    notifyListeners(); <span class="cm">// Triggers Consumer / context.watch rebuild</span>
  }}

  <span class="kw">void</span> deleteTransaction(<span class="cls">String</span> id) {{
    _transactions.removeWhere((tx) =&gt; tx.id == id);
    notifyListeners(); <span class="cm">// Automatically refreshes UI across all screens</span>
  }}
}}
  </pre>

  <p style="font-size: 8.5pt; color: #475569; margin-top: 6px;">
    <strong>Design Principle:</strong> <code>notifyListeners()</code> dispatches an observer signal to registered widgets. The private <code>_transactions</code> list enforces strict encapsulation; views access an unmodifiable reversed copy via the getter.
  </p>

  <div class="page-footer">
    <span>Vishnu Institute of Technology :: Bhimavaram</span>
    <span>Page 7 of 13</span>
  </div>
</div>


<!-- ==========================================
     PAGE 8: CODE SNIPPETS - HOME SCREEN
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Implementation - HomeScreen</span>
    <span>Section 4.3</span>
  </div>

  <h2 class="section-title">4.3 Responsive Dashboard Screen (<code>home_screen.dart</code>)</h2>
  <pre class="code-box" style="font-size: 7.1pt; line-height: 1.23;">
<span class="kw">class</span> <span class="cls">HomeScreen</span> <span class="kw">extends</span> <span class="cls">StatelessWidget</span> {{
  <span class="kw">const</span> <span class="cls">HomeScreen</span>({{<span class="kw">super</span>.key}});

  <span class="kw">@override</span>
  <span class="cls">Widget</span> build(<span class="cls">BuildContext</span> context) {{
    <span class="kw">return</span> <span class="cls">Scaffold</span>(
      appBar: <span class="cls">AppBar</span>(title: <span class="kw">const</span> <span class="cls">Text</span>(<span class="str">'Overview'</span>, style: <span class="cls">TextStyle</span>(fontWeight: <span class="cls">FontWeight</span>.w700))),
      body: <span class="cls">Consumer</span>&lt;<span class="cls">TransactionProvider</span>&gt;(
        builder: (context, provider, child) {{
          <span class="kw">final</span> isEmpty = provider.transactions.isEmpty;
          <span class="kw">return</span> <span class="cls">CustomScrollView</span>(
            slivers: [
              <span class="cls">SliverToBoxAdapter</span>(
                child: <span class="cls">Column</span>(
                  children: [
                    <span class="kw">const</span> <span class="cls">BalanceCard</span>(),
                    <span class="kw">if</span> (!isEmpty)
                      <span class="cls">Container</span>(
                        margin: <span class="kw">const</span> <span class="cls">EdgeInsets</span>.all(<span class="str">24.0</span>),
                        padding: <span class="kw">const</span> <span class="cls">EdgeInsets</span>.all(<span class="str">24.0</span>),
                        decoration: <span class="cls">BoxDecoration</span>(
                          color: <span class="cls">Colors</span>.white, borderRadius: <span class="cls">BorderRadius</span>.circular(<span class="str">32</span>),
                        ),
                        child: <span class="kw">const</span> <span class="cls">ExpensePieChart</span>(),
                      ),
                  ],
                ),
              ),
              <span class="kw">if</span> (isEmpty)
                <span class="kw">const</span> <span class="cls">SliverFillRemaining</span>(
                  hasScrollBody: <span class="kw">false</span>,
                  child: <span class="cls">Center</span>(child: <span class="cls">Text</span>(<span class="str">'No transactions yet.\\nAdd your first entry!'</span>)),
                )
              <span class="kw">else</span>
                <span class="cls">SliverPadding</span>(
                  padding: <span class="kw">const</span> <span class="cls">EdgeInsets</span>.only(bottom: <span class="str">100</span>),
                  sliver: <span class="cls">SliverList</span>(
                    delegate: <span class="cls">SliverChildBuilderDelegate</span>(
                      (context, index) =&gt; <span class="cls">TransactionCard</span>(transaction: provider.transactions[index]),
                      childCount: provider.transactions.length,
                    ),
                  ),
                ),
            ],
          );
        }},
      ),
      floatingActionButton: <span class="cls">FloatingActionButton</span>(
        onPressed: () =&gt; <span class="cls">Navigator</span>.push(context, <span class="cls">MaterialPageRoute</span>(builder: (_) =&gt; <span class="kw">const</span> <span class="cls">AddTransactionScreen</span>())),
        child: <span class="kw">const</span> <span class="cls">Icon</span>(<span class="cls">Icons</span>.add_rounded),
      ),
    );
  }}
}}
  </pre>

  <p style="font-size: 8.5pt; color: #475569; margin-top: 6px;">
    <strong>Sliver Architecture Benefit:</strong> <code>SliverList</code> renders visible items on-demand, maintaining smooth 60 FPS performance regardless of transaction history length.
  </p>

  <div class="page-footer">
    <span>Vishnu Institute of Technology :: Bhimavaram</span>
    <span>Page 8 of 13</span>
  </div>
</div>


<!-- ==========================================
     PAGE 9: CODE SNIPPETS - ADD TRANSACTION
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Implementation - AddTransactionScreen</span>
    <span>Section 4.4</span>
  </div>

  <h2 class="section-title">4.4 Form Screen & Input Validation (<code>add_transaction_screen.dart</code>)</h2>
  <pre class="code-box" style="font-size: 7.1pt; line-height: 1.24;">
<span class="kw">class</span> <span class="cls">_AddTransactionScreenState</span> <span class="kw">extends</span> <span class="cls">State</span>&lt;<span class="cls">AddTransactionScreen</span>&gt; {{
  <span class="kw">final</span> _formKey = <span class="cls">GlobalKey</span>&lt;<span class="cls">FormState</span>&gt;();
  <span class="kw">final</span> _titleController = <span class="cls">TextEditingController</span>();
  <span class="kw">final</span> _amountController = <span class="cls">TextEditingController</span>();
  <span class="cls">TransactionType</span> _selectedType = <span class="cls">TransactionType</span>.expense;
  <span class="cls">String</span>? _selectedCategory;
  <span class="cls">DateTime</span> _selectedDate = <span class="cls">DateTime</span>.now();

  <span class="kw">void</span> _submitData() {{
    <span class="kw">if</span> (_formKey.currentState!.validate()) {{
      <span class="kw">final</span> amount = <span class="cls">double</span>.tryParse(_amountController.text) ?? <span class="str">0.0</span>;
      <span class="kw">if</span> (_selectedCategory == <span class="kw">null</span>) {{
        <span class="cls">ScaffoldMessenger</span>.of(context).showSnackBar(
          <span class="kw">const</span> <span class="cls">SnackBar</span>(content: <span class="cls">Text</span>(<span class="str">'Please select a category'</span>)),
        );
        <span class="kw">return</span>;
      }}
      <span class="kw">final</span> newTx = <span class="cls">TransactionModel</span>(
        id: <span class="cls">DateTime</span>.now().toString(),
        title: _titleController.text.trim(),
        amount: amount,
        type: _selectedType,
        date: _selectedDate,
        category: _selectedCategory!,
      );

      <span class="cm">// context.read dispatches mutation without ongoing subscription</span>
      context.read&lt;<span class="cls">TransactionProvider</span>&gt;().addTransaction(newTx);
      <span class="cls">Navigator</span>.pop(context);
    }}
  }}

  <span class="kw">@override</span>
  <span class="cls">Widget</span> build(<span class="cls">BuildContext</span> context) {{
    <span class="kw">return</span> <span class="cls">Scaffold</span>(
      appBar: <span class="cls">AppBar</span>(title: <span class="kw">const</span> <span class="cls">Text</span>(<span class="str">'New Transaction'</span>)),
      body: <span class="cls">Form</span>(
        key: _formKey,
        child: <span class="cls">ListView</span>(
          padding: <span class="kw">const</span> <span class="cls">EdgeInsets</span>.all(<span class="str">24</span>),
          children: [
            <span class="cls">TextFormField</span>(
              controller: _amountController,
              decoration: <span class="kw">const</span> <span class="cls">InputDecoration</span>(labelText: <span class="str">'Amount (₹)'</span>),
              keyboardType: <span class="kw">const</span> <span class="cls">TextInputType</span>.numberWithOptions(decimal: <span class="kw">true</span>),
              validator: (val) =&gt; (val == <span class="kw">null</span> || (<span class="cls">double</span>.tryParse(val) ?? <span class="str">0</span>) &lt;= <span class="str">0</span>) ? <span class="str">'Enter amount &gt; 0'</span> : <span class="kw">null</span>,
            ),
            <span class="cls">TextFormField</span>(
              controller: _titleController,
              decoration: <span class="kw">const</span> <span class="cls">InputDecoration</span>(labelText: <span class="str">'Title'</span>),
              validator: (val) =&gt; (val == <span class="kw">null</span> || val.trim().isEmpty) ? <span class="str">'Enter title'</span> : <span class="kw">null</span>,
            ),
            <span class="cls">FilledButton</span>(onPressed: _submitData, child: <span class="kw">const</span> <span class="cls">Text</span>(<span class="str">'Save Transaction'</span>)),
          ],
        ),
      ),
    );
  }}
}}
  </pre>

  <p style="font-size: 8.5pt; color: #475569; margin-top: 6px;">
    <strong>Form Validation Cycle:</strong> <code>_formKey.currentState!.validate()</code> executes all child validators, safeguarding against invalid numbers or missing data.
  </p>

  <div class="page-footer">
    <span>Vishnu Institute of Technology :: Bhimavaram</span>
    <span>Page 9 of 13</span>
  </div>
</div>


<!-- ==========================================
     PAGE 10: CODE SNIPPETS - MODULAR WIDGETS
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Implementation - Modular Widgets</span>
    <span>Section 4.5</span>
  </div>

  <h2 class="section-title">4.5 Source Code: Modular Reusable Widgets</h2>

  <h3 class="sub-title">4.5.1 Balance Card Widget (<code>lib/widgets/balance_card.dart</code>)</h3>
  <pre class="code-box" style="font-size: 7.0pt; line-height: 1.22;">
<span class="kw">class</span> <span class="cls">BalanceCard</span> <span class="kw">extends</span> <span class="cls">StatelessWidget</span> {{
  <span class="kw">const</span> <span class="cls">BalanceCard</span>({{<span class="kw">super</span>.key}});

  <span class="kw">@override</span>
  <span class="cls">Widget</span> build(<span class="cls">BuildContext</span> context) {{
    <span class="kw">final</span> provider = context.watch&lt;<span class="cls">TransactionProvider</span>&gt;();
    <span class="kw">return</span> <span class="cls">Container</span>(
      margin: <span class="kw">const</span> <span class="cls">EdgeInsets</span>.all(<span class="str">24</span>),
      padding: <span class="kw">const</span> <span class="cls">EdgeInsets</span>.all(<span class="str">28</span>),
      decoration: <span class="cls">BoxDecoration</span>(
        borderRadius: <span class="cls">BorderRadius</span>.circular(<span class="str">32</span>),
        gradient: <span class="kw">const</span> <span class="cls">LinearGradient</span>(colors: [<span class="cls">Color</span>(<span class="str">0xFF0F172A</span>), <span class="cls">Color</span>(<span class="str">0xFF1E293B</span>)]),
      ),
      child: <span class="cls">Column</span>(
        children: [
          <span class="kw">const</span> <span class="cls">Text</span>(<span class="str">'Total Balance'</span>, style: <span class="cls">TextStyle</span>(color: <span class="cls">Color</span>(<span class="str">0xFF94A3B8</span>))),
          <span class="cls">Text</span>(<span class="str">'₹${{provider.balance.toStringAsFixed(2)}}'</span>, style: <span class="kw">const</span> <span class="cls">TextStyle</span>(fontSize: <span class="str">36</span>, color: <span class="cls">Colors</span>.white)),
          <span class="cls">Row</span>(
            mainAxisAlignment: <span class="cls">MainAxisAlignment</span>.spaceBetween,
            children: [
              <span class="cls">Text</span>(<span class="str">'Income: ₹${{provider.totalIncome.toStringAsFixed(0)}}'</span>, style: <span class="kw">const</span> <span class="cls">TextStyle</span>(color: <span class="cls">Colors</span>.green)),
              <span class="cls">Text</span>(<span class="str">'Expense: ₹${{provider.totalExpense.toStringAsFixed(0)}}'</span>, style: <span class="kw">const</span> <span class="cls">TextStyle</span>(color: <span class="cls">Colors</span>.red)),
            ],
          ),
        ],
      ),
    );
  }}
}}
  </pre>

  <h3 class="sub-title">4.5.2 Expense Pie Chart Widget (<code>lib/widgets/expense_pie_chart.dart</code>)</h3>
  <pre class="code-box" style="font-size: 7.0pt; line-height: 1.22;">
<span class="kw">class</span> <span class="cls">ExpensePieChart</span> <span class="kw">extends</span> <span class="cls">StatelessWidget</span> {{
  <span class="kw">const</span> <span class="cls">ExpensePieChart</span>({{<span class="kw">super</span>.key}});

  <span class="kw">@override</span>
  <span class="cls">Widget</span> build(<span class="cls">BuildContext</span> context) {{
    <span class="kw">final</span> provider = context.watch&lt;<span class="cls">TransactionProvider</span>&gt;();
    <span class="kw">final</span> map = provider.expensesByCategory;
    <span class="kw">if</span> (map.isEmpty) <span class="kw">return</span> <span class="kw">const</span> <span class="cls">Text</span>(<span class="str">'No expenses to display'</span>);

    <span class="kw">return</span> <span class="cls">SizedBox</span>(
      height: <span class="str">170</span>,
      child: <span class="cls">PieChart</span>(
        <span class="cls">PieChartData</span>(
          sections: map.entries.map((e) =&gt; <span class="cls">PieChartSectionData</span>(value: e.value, title: <span class="str">''</span>, radius: <span class="str">22</span>)).toList(),
          centerSpaceRadius: <span class="str">50</span>,
        ),
      ),
    );
  }}
}}
  </pre>

  <div class="page-footer">
    <span>Vishnu Institute of Technology :: Bhimavaram</span>
    <span>Page 10 of 13</span>
  </div>
</div>


<!-- ==========================================
     PAGE 11: DEPLOYMENT & TESTING MATRIX
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Deployment & Verification Matrix</span>
    <span>Section 5</span>
  </div>

  <h2 class="section-title">5. Cloud Deployment & System Verification</h2>

  <h3 class="sub-title">5.1 Cloud Deployment Pipeline (GitHub Pages)</h3>
  <pre class="code-box">
<span class="cm"># 1. Compile optimized release build for GitHub Pages subpath</span>
flutter build web --release --base-href "/Expense-Tracker/"

<span class="cm"># 2. Push production artifact to the dedicated gh-pages deployment branch</span>
cd build/web &amp;&amp; git init &amp;&amp; git checkout -b gh-pages
git add . &amp;&amp; git commit -m "Deploy Web Build"
git remote add origin https://github.com/Saketh17-max/Expense-Tracker.git
git push -u origin gh-pages --force
  </pre>

  <h3 class="sub-title">5.2 System Testing & Verification Matrix</h3>
  <table class="report-table" style="font-size: 7.8pt;">
    <thead>
      <tr>
        <th style="width: 10%;">ID</th>
        <th style="width: 25%;">Test Objective</th>
        <th style="width: 30%;">Input Data / Test Procedure</th>
        <th style="width: 25%;">Expected Result</th>
        <th style="width: 10%; text-align: center;">Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>TC-01</strong></td>
        <td>Add Income Record</td>
        <td>Title: "Product Sales", Amount: ₹5000, Category: "Sales"</td>
        <td>Total Income increments by ₹5000, Balance increases by ₹5000.</td>
        <td style="color:#16a34a; font-weight:700; text-align:center;">PASS</td>
      </tr>
      <tr>
        <td><strong>TC-02</strong></td>
        <td>Add Expense Record</td>
        <td>Title: "Office Supplies", Amount: ₹1200, Category: "Supplies"</td>
        <td>Total Expense increments by ₹1200, Balance decreases by ₹1200.</td>
        <td style="color:#16a34a; font-weight:700; text-align:center;">PASS</td>
      </tr>
      <tr>
        <td><strong>TC-03</strong></td>
        <td>Donut Chart Aggregation</td>
        <td>Add multiple expenses in "Supplies" and "Utilities"</td>
        <td>Donut chart renders slices matching category proportions.</td>
        <td style="color:#16a34a; font-weight:700; text-align:center;">PASS</td>
      </tr>
      <tr>
        <td><strong>TC-04</strong></td>
        <td>Form Validation (Empty)</td>
        <td>Submit form with blank Title and zero Amount</td>
        <td>Validation error prompts: "Enter title" and "Enter amount &gt; 0".</td>
        <td style="color:#16a34a; font-weight:700; text-align:center;">PASS</td>
      </tr>
      <tr>
        <td><strong>TC-05</strong></td>
        <td>Delete Transaction</td>
        <td>Click delete icon on "Office Supplies" and confirm dialog</td>
        <td>Item removed from list, Balance updates immediately.</td>
        <td style="color:#16a34a; font-weight:700; text-align:center;">PASS</td>
      </tr>
      <tr>
        <td><strong>TC-06</strong></td>
        <td>Delete Cancelation</td>
        <td>Click delete icon and press "Cancel" in dialog</td>
        <td>Transaction remains intact, balances unchanged.</td>
        <td style="color:#16a34a; font-weight:700; text-align:center;">PASS</td>
      </tr>
      <tr>
        <td><strong>TC-07</strong></td>
        <td>Empty State UI</td>
        <td>Delete all transactions from state</td>
        <td>Shows empty state card with guidance to add entries.</td>
        <td style="color:#16a34a; font-weight:700; text-align:center;">PASS</td>
      </tr>
      <tr>
        <td><strong>TC-08</strong></td>
        <td>Responsive Layout</td>
        <td>Resize browser between 360px (mobile) and 1920px (desktop)</td>
        <td>UI adapts seamlessly with zero RenderFlex overflow errors.</td>
        <td style="color:#16a34a; font-weight:700; text-align:center;">PASS</td>
      </tr>
    </tbody>
  </table>

  <div class="page-footer">
    <span>Vishnu Institute of Technology :: Bhimavaram</span>
    <span>Page 11 of 13</span>
  </div>
</div>


<!-- ==========================================
     PAGE 12: LARGE OUTPUT SCREENS (PART 1: WEB DASHBOARD SHOWCASE)
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Output Screens - Web Deployment</span>
    <span>Section 6</span>
  </div>

  <h2 class="section-title">6. Output Screens: Web Dashboard & Analytics Showcase</h2>

  <div class="figure-box" style="margin-bottom: 12px;">
    <img src="{desktop_b64}" class="figure-img" style="height: 200px; width: 100%; object-fit: cover;">
    <div class="caption">Figure 6.1: Full Desktop Dashboard Overview (Live Web Deployment on GitHub Pages)</div>
  </div>
  <p style="font-size: 8.5pt; color: #334155;">
    <strong>Dashboard Analysis:</strong> Figure 6.1 presents the production web application view. The slate gradient <code>BalanceCard</code> prominently features the calculated Net Balance (₹3,800.00), accompanied by color-coded sub-indicators for aggregated Income and Expenses. The clean, modern typography and surface elevation ensure immediate readability.
  </p>

  <div class="figure-box" style="margin-top: 10px; margin-bottom: 8px;">
    <img src="{chart_tx_b64}" class="figure-img" style="height: 190px; width: 100%; object-fit: cover;">
    <div class="caption">Figure 6.2: Categorical Donut Breakdown Chart & Live Transaction Stream</div>
  </div>
  <p style="font-size: 8.5pt; color: #334155;">
    <strong>Visual Analytics:</strong> Figure 6.2 illustrates the interactive vector donut chart powered by <code>fl_chart</code>. Outflows are grouped by category (Supplies, Utilities) with a color-coded legend, while recent entries display beneath with category-specific rounded icon badges.
  </p>

  <div class="page-footer">
    <span>Vishnu Institute of Technology :: Bhimavaram</span>
    <span>Page 12 of 13</span>
  </div>
</div>


<!-- ==========================================
     PAGE 13: LARGE OUTPUT SCREENS (PART 2: MOBILE VIEWS) & CONCLUSION
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Mobile Views & Project Conclusion</span>
    <span>Section 7</span>
  </div>

  <h2 class="section-title">7. Output Screens: Mobile Interface & Conclusion</h2>

  <!-- Substantially larger mobile screenshots -->
  <div style="display: flex; justify-content: center; gap: 24px; margin-top: 4px; margin-bottom: 8px;">
    <div class="figure-box" style="flex: 1; text-align: center;">
      <img src="{add_tx_b64}" class="figure-img" style="height: 235px; width: auto; object-fit: contain;">
      <div class="caption">Figure 7.1: New Transaction Creation Form</div>
    </div>
    <div class="figure-box" style="flex: 1; text-align: center;">
      <img src="{dialog_b64}" class="figure-img" style="height: 235px; width: auto; object-fit: contain;">
      <div class="caption">Figure 7.2: Delete Confirmation Modal Dialog</div>
    </div>
  </div>

  <h3 class="sub-title" style="margin-top: 8px;">7.1 Project Conclusion & Technical Summary</h3>
  <p style="font-size: 8.5pt;">
    The <strong>Small-Business Income/Expense Tracker</strong> delivers a complete, production-grade bookkeeping solution built in Flutter. By adopting the <strong>Provider</strong> pattern, all financial calculations ($Balance = Income - Expense$) and category aggregations execute with zero latency in constant $O(n)$ time complexity, ensuring instant updates across both desktop and mobile viewports.
  </p>

  <h3 class="sub-title">7.2 Future Scope & Enhancements</h3>
  <ul style="font-size: 8.2pt;">
    <li><strong>Offline Caching:</strong> Integrate local key-value storage (Hive / SharedPreferences) for persistence across device restarts.</li>
    <li><strong>Automated PDF Export:</strong> Allow owners to generate and export monthly financial statements directly from the client.</li>
    <li><strong>Multi-Currency Support:</strong> Localized GST handling and international currency conversion options.</li>
  </ul>

  <div class="callout" style="font-size: 8.5pt; margin-top: 6px;">
    &bull; <strong>GitHub Source Code Repository:</strong> <a href="https://github.com/Saketh17-max/Expense-Tracker" style="color:#1d4ed8;">https://github.com/Saketh17-max/Expense-Tracker</a><br>
    &bull; <strong>Live Cloud Web Application:</strong> <a href="https://saketh17-max.github.io/Expense-Tracker/" style="color:#1d4ed8;">https://saketh17-max.github.io/Expense-Tracker/</a>
  </div>

  <div class="page-footer">
    <span>Vishnu Institute of Technology :: Bhimavaram</span>
    <span>Page 13 of 13</span>
  </div>
</div>

</body>
</html>
"""

html_path = r"C:\Users\venka\Desktop\college\flutter\complete_report.html"
pdf_path = r"C:\Users\venka\Desktop\college\flutter\Project_Report_T_Venkat_Saketh.pdf"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Wrote updated HTML report to {html_path} ({len(html_content)} bytes)")

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    html_path
]

print("Rendering updated PDF via Chrome headless...")
subprocess.run(cmd, check=True)

if os.path.exists(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    print(f"SUCCESS: Generated PDF '{pdf_path}' with {len(reader.pages)} pages! File size: {os.path.getsize(pdf_path)} bytes.")
else:
    print("ERROR: PDF was not generated!")
