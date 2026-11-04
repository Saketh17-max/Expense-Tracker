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
mobile_b64 = get_base64_img(os.path.join(assets_dir, "mobile_overview.png"))
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
    font-size: 9.5pt;
    line-height: 1.45;
  }}
  .page {{
    width: 210mm;
    height: 297mm;
    min-height: 297mm;
    max-height: 297mm;
    position: relative;
    background: #ffffff;
    padding: 22mm 20mm 26mm 20mm;
    page-break-after: always;
    page-break-inside: avoid;
    overflow: hidden;
    margin: 0 auto;
  }}
  
  /* Running Header & Footer */
  .page-header {{
    position: absolute;
    top: 9mm;
    left: 20mm;
    right: 20mm;
    height: 8mm;
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
    font-size: 13.5pt;
    color: #1e3a8a;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 4px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  h3.sub-title {{
    font-size: 10.5pt;
    color: #0f172a;
    margin-top: 8px;
    margin-bottom: 5px;
  }}
  .badge {{
    background: #eff6ff;
    color: #1d4ed8;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 7.5pt;
    font-weight: 700;
    text-transform: uppercase;
  }}
  
  /* Tables */
  table.report-table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 6px;
    margin-bottom: 10px;
    font-size: 8.5pt;
  }}
  table.report-table th {{
    background: #1e3a8a;
    color: #ffffff;
    font-weight: 600;
    text-align: left;
    padding: 6px 10px;
    border: 1px solid #1e3a8a;
  }}
  table.report-table td {{
    padding: 5px 10px;
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
    padding: 8px 12px;
    font-family: Consolas, "Courier New", monospace;
    font-size: 7.2pt;
    line-height: 1.25;
    color: #0f172a;
    overflow: hidden;
    margin-top: 5px;
    margin-bottom: 8px;
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
    padding: 8px 12px;
    border-radius: 6px;
    margin: 6px 0;
    font-size: 8.5pt;
  }}
  .callout-title {{
    font-weight: 700;
    color: #1e3a8a;
    margin-bottom: 3px;
  }}
  
  /* Image figure containers */
  .figure-box {{
    text-align: center;
    margin: 6px 0;
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
    margin-top: 3px;
    margin-bottom: 6px;
    text-align: justify;
  }}
  ul, ol {{
    margin-top: 3px;
    margin-bottom: 6px;
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

  <!-- Student Name and Roll No in the requested space -->
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
     PAGE 2: TABLE OF CONTENTS
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
        <td><strong>Student Details & Comprehensive Project Metadata</strong></td>
        <td style="text-align: center; font-weight: 700;">3</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: 700;">2</td>
        <td><strong>Project Title, Background & Problem Definition</strong></td>
        <td style="text-align: center; font-weight: 700;">3</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: 700;">3</td>
        <td><strong>Project Objectives & System Scope</strong></td>
        <td style="text-align: center; font-weight: 700;">4</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: 700;">4</td>
        <td><strong>Technology Stack & Key Flutter Concepts Demonstrated</strong></td>
        <td style="text-align: center; font-weight: 700;">5</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: 700;">5</td>
        <td><strong>System Architecture & Reactive State Management Model</strong></td>
        <td style="text-align: center; font-weight: 700;">6</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: 700;">6</td>
        <td><strong>Project Directory Structure & Component Organization</strong></td>
        <td style="text-align: center; font-weight: 700;">7</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: 700;">7</td>
        <td><strong>Detailed Implementation & Code Snippets:</strong></td>
        <td style="text-align: center; font-weight: 700;">8 - 12</td>
      </tr>
      <tr>
        <td style="text-align: center;">7.1</td>
        <td style="padding-left: 20px;">Application Root & Global Theming (<code>lib/main.dart</code>)</td>
        <td style="text-align: center;">8</td>
      </tr>
      <tr>
        <td style="text-align: center;">7.2</td>
        <td style="padding-left: 20px;">Transaction Domain Data Model (<code>lib/models/transaction.dart</code>)</td>
        <td style="text-align: center;">8</td>
      </tr>
      <tr>
        <td style="text-align: center;">7.3</td>
        <td style="padding-left: 20px;">State Management Controller (<code>lib/providers/transaction_provider.dart</code>)</td>
        <td style="text-align: center;">9</td>
      </tr>
      <tr>
        <td style="text-align: center;">7.4</td>
        <td style="padding-left: 20px;">Responsive Dashboard Screen (<code>lib/screens/home_screen.dart</code>)</td>
        <td style="text-align: center;">10</td>
      </tr>
      <tr>
        <td style="text-align: center;">7.5</td>
        <td style="padding-left: 20px;">Transaction Form & Input Validation (<code>lib/screens/add_transaction_screen.dart</code>)</td>
        <td style="text-align: center;">11</td>
      </tr>
      <tr>
        <td style="text-align: center;">7.6</td>
        <td style="padding-left: 20px;">Modular Widgets: Balance Card & Category Pie Chart</td>
        <td style="text-align: center;">12</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: 700;">8</td>
        <td><strong>Cloud Deployment, Hosting & Continuous Delivery (GitHub Pages)</strong></td>
        <td style="text-align: center; font-weight: 700;">13</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: 700;">9</td>
        <td><strong>System Verification, Test Cases & Validation Matrix</strong></td>
        <td style="text-align: center; font-weight: 700;">13</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: 700;">10</td>
        <td><strong>Output Screens, Interactive Visualizations & User Workflow</strong></td>
        <td style="text-align: center; font-weight: 700;">14</td>
      </tr>
      <tr>
        <td style="text-align: center; font-weight: 700;">11</td>
        <td><strong>Project Conclusion & Technical Summary</strong></td>
        <td style="text-align: center; font-weight: 700;">15</td>
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
    <span>Page 2 of 15</span>
  </div>
</div>


<!-- ==========================================
     PAGE 3: STUDENT DETAILS & PROBLEM DEFINITION
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Student Details & Project Title</span>
    <span>Section 1 & 2</span>
  </div>

  <h2 class="section-title">1. Student Details & Project Profile</h2>
  
  <table class="report-table">
    <tr>
      <th style="width: 30%;">Field</th>
      <th style="width: 70%;">Academic Information</th>
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
      <td><strong>Department</strong></td>
      <td>Computer Science and Engineering (CSE)</td>
    </tr>
    <tr>
      <td><strong>Class Section</strong></td>
      <td>Section D</td>
    </tr>
    <tr>
      <td><strong>Course Title</strong></td>
      <td>User Interface Design Using Flutter</td>
    </tr>
    <tr>
      <td><strong>Course Instructor</strong></td>
      <td>Mrs. P. Shyamala Madhuri, Assistant Professor, Dept. of CSE</td>
    </tr>
    <tr>
      <td><strong>Head of Department</strong></td>
      <td>Dr. R. Srinivasa Raju, Professor & HOD, Dept. of CSE</td>
    </tr>
    <tr>
      <td><strong>Institution</strong></td>
      <td>Vishnu Institute of Technology (Autonomous), Bhimavaram</td>
    </tr>
  </table>

  <h2 class="section-title" style="margin-top: 12px;">2. Project Title & Problem Statement</h2>

  <div class="callout">
    <div class="callout-title">Formal Project Title</div>
    <div style="font-weight: 700; color: #0f172a; font-size: 9.5pt;">
      "Create a small-business income/expense tracker with balance summary using Provider."
    </div>
  </div>

  <h3 class="sub-title">2.1 Background & Context</h3>
  <p>
    Micro and small enterprises form the economic backbone of developing communities. Small retail stores, freelance operators, repair technicians, and local service providers execute dozens of micro-transactions daily. Despite the critical requirement for cash flow clarity, most small-business owners continue to rely on manual paper ledgers or memory, leading to calculation inaccuracies, lack of cash visibility, and operational confusion.
  </p>

  <h3 class="sub-title">2.2 Core Problem Definition</h3>
  <ul>
    <li><strong>Arithmetic Inaccuracies:</strong> Frequent manual computation errors occur when adding running expenses against revenue, distorting actual cash positions.</li>
    <li><strong>Lack of Real-time Cash Visibility:</strong> Owners cannot instantly tell if their business is operating at a net profit or deficit at any given hour.</li>
    <li><strong>Absence of Expenditure Categorization:</strong> Without spending categorization (Supplies, Utilities, Transport, Food), owners cannot identify operational leakages.</li>
    <li><strong>Overly Complex Existing Solutions:</strong> Mainstream accounting packages require complex accounting knowledge, cloud logins, backend servers, and subscription fees.</li>
  </ul>

  <h3 class="sub-title">2.3 Proposed Solution</h3>
  <p>
    An intuitive, lightweight, offline-capable mobile and web application built in Flutter using the <strong>Provider</strong> architecture. It delivers instant net balance calculation, visual donut breakdown charts, and seamless transaction creation and deletion with strict client validation.
  </p>

  <div class="page-footer">
    <span>Vishnu Institute of Technology :: Bhimavaram</span>
    <span>Page 3 of 15</span>
  </div>
</div>


<!-- ==========================================
     PAGE 4: PROJECT OBJECTIVES & SYSTEM SCOPE (NO SDG 8)
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Project Objectives & System Scope</span>
    <span>Section 3</span>
  </div>

  <h2 class="section-title">3. Project Objectives & System Scope</h2>

  <h3 class="sub-title">3.1 Primary Functional Objectives</h3>
  <ul>
    <li><strong>Streamlined Financial Recording:</strong> Provide a clean, guided form allowing business owners to input transaction titles, monetary amounts in Indian Rupees (₹), transaction categories, and accurate calendar dates.</li>
    <li><strong>Automated Real-Time Financial Balance:</strong> Dynamically compute and display the total accumulated income, total aggregated expenses, and the resultant net balance ($Balance = Income - Expense$) without manual recalculation.</li>
    <li><strong>Categorical Visual Analytics:</strong> Generate interactive graphical donut charts utilizing vector graphics (<code>fl_chart</code>) to display expenditure distribution across categories (Food, Transport, Utilities, Supplies, Other).</li>
    <li><strong>Safe Transaction Management:</strong> Allow users to audit historical entries in a chronological feed and delete erroneous records with an explicit dialog confirmation.</li>
    <li><strong>Strict Client-Side Validation:</strong> Enforce rigorous validation rules to eliminate empty titles, negative quantities, zero amounts, and unselected classifications.</li>
  </ul>

  <h3 class="sub-title">3.2 Technical & Architectural Objectives</h3>
  <ul>
    <li><strong>Pure Provider Architecture:</strong> Strictly manage application state using Flutter's official <code>ChangeNotifier</code> and <code>ChangeNotifierProvider</code> paradigm, eliminating global variables, state leakage, or heavyweight enterprise BLoC/Redux boilerplate.</li>
    <li><strong>Modular Component Structure:</strong> Structure the codebase into modular, single-responsibility files that allow a 2nd-year computer science undergraduate to easily defend and explain every architectural decision during academic viva examination.</li>
    <li><strong>Zero-Backend Simplicity:</strong> Achieve 100% reactive client-side performance without external databases, third-party authentication, or remote APIs, ensuring instant startup on both Android and Web.</li>
  </ul>

  <h3 class="sub-title">3.3 System Scope & Target Users</h3>
  <p>
    The application is engineered specifically for sole proprietorships, retail shopkeepers, independent contractors, and freelance service providers who require an unencumbered, high-speed bookkeeping tool. The system operates directly in the browser or on mobile devices with zero configuration overhead, providing immediate cash flow tracking and visual financial clarity.
  </p>

  <h3 class="sub-title">3.4 Key System Boundaries</h3>
  <ul>
    <li><strong>Platform Support:</strong> Fully cross-platform, tested and deployed across Web (Chrome, Edge, Safari) and Android smartphones.</li>
    <li><strong>Data Handling:</strong> In-memory reactive state managed securely via Provider, optimized for quick daily reconciliation.</li>
    <li><strong>Visual Feedback:</strong> Instantaneous reactive updates across all widgets without manual screen refreshes.</li>
  </ul>

  <div class="page-footer">
    <span>Vishnu Institute of Technology :: Bhimavaram</span>
    <span>Page 4 of 15</span>
  </div>
</div>


<!-- ==========================================
     PAGE 5: TECHNOLOGY STACK & CONCEPTS
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Technology Stack & Flutter Concepts</span>
    <span>Section 4</span>
  </div>

  <h2 class="section-title">4. Technology Stack & Key Flutter Concepts</h2>

  <h3 class="sub-title">4.1 Technology Specifications</h3>
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

  <h3 class="sub-title">4.2 Fundamental Flutter Concepts Demonstrated</h3>
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
    <span>Page 5 of 15</span>
  </div>
</div>


<!-- ==========================================
     PAGE 6: SYSTEM ARCHITECTURE & STATE MODEL
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>System Architecture & State Model</span>
    <span>Section 5</span>
  </div>

  <h2 class="section-title">5. System Architecture & Reactive State Management</h2>

  <div class="figure-box">
    <img src="{arch_b64}" class="figure-img" style="height: 185px; width: auto;">
    <div class="caption">Figure 5.1: High-Level Unidirectional Architecture and Provider Reactive Loop</div>
  </div>

  <h3 class="sub-title">5.1 Layered Architectural Decomposition</h3>
  <ol>
    <li><strong>Data Model Layer:</strong> Encapsulates pure domain representations. The <code>TransactionModel</code> class models individual ledger records, while the <code>TransactionType</code> enumeration defines immutable debit/credit types.</li>
    <li><strong>State Management Layer (Business Logic):</strong> Centered around <code>TransactionProvider</code>, which mixes in <code>ChangeNotifier</code>. This layer acts as the single source of truth for calculations, maintaining the private transaction list and exposing read-only getters.</li>
    <li><strong>Presentation Layer (UI):</strong> Divided into top-level screens (<code>HomeScreen</code>, <code>AddTransactionScreen</code>) and reusable atomic widgets (<code>BalanceCard</code>, <code>ExpensePieChart</code>, <code>TransactionCard</code>).</li>
  </ol>

  <h3 class="sub-title">5.2 The Provider Reactive Lifecycle</h3>
  <ul>
    <li><strong>State Dispatch:</strong> When a user submits a valid transaction, the view invokes <code>context.read&lt;TransactionProvider&gt;().addTransaction(newTx)</code> to dispatch the action without establishing a redundant persistent listener.</li>
    <li><strong>State Mutation & Notification:</strong> The provider mutates its internal <code>_transactions</code> collection and immediately executes <code>notifyListeners()</code>.</li>
    <li><strong>Selective Re-rendering:</strong> Flutter's widget tree detects the notification. Widgets wrapped in <code>Consumer&lt;TransactionProvider&gt;</code> or invoking <code>context.watch&lt;TransactionProvider&gt;()</code> execute their <code>build()</code> methods, updating only the affected subtrees.</li>
  </ul>

  <div class="page-footer">
    <span>Vishnu Institute of Technology :: Bhimavaram</span>
    <span>Page 6 of 15</span>
  </div>
</div>


<!-- ==========================================
     PAGE 7: PROJECT STRUCTURE & ORGANIZATION
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Project Structure & Organization</span>
    <span>Section 6</span>
  </div>

  <h2 class="section-title">6. Project Directory Structure & Organization</h2>

  <h3 class="sub-title">6.1 File Tree Organization</h3>
  <pre class="code-box" style="font-size: 7.6pt; line-height: 1.25;">
lib/
&#9474;
&#9500;&#9472;&#9472; main.dart                      &larr; Application entry point, global theme & Provider root
&#9500;&#9472;&#9472; models/
&#9474;   &#9492;&#9472;&#9472; transaction.dart           &larr; TransactionModel class & TransactionType enum
&#9500;&#9472;&#9472; providers/
&#9474;   &#9492;&#9472;&#9472; transaction_provider.dart  &larr; ChangeNotifier managing business logic & state
&#9500;&#9472;&#9472; screens/
&#9474;   &#9500;&#9472;&#9472; home_screen.dart           &larr; Primary dashboard with overview cards & charts
&#9474;   &#9492;&#9472;&#9472; add_transaction_screen.dart&larr; Form screen with segmented control & validation
&#9492;&#9472;&#9472; widgets/
    &#9500;&#9472;&#9472; balance_card.dart          &larr; Modern gradient card displaying Net Balance
    &#9500;&#9472;&#9472; summary_card.dart          &larr; Reusable mini statistical badge widget
    &#9500;&#9472;&#9472; expense_pie_chart.dart     &larr; Donut chart visualizer for categorized spending
    &#9492;&#9472;&#9472; transaction_card.dart      &larr; ListTile card with category icons & delete modal
  </pre>

  <h3 class="sub-title">6.2 Architectural Role of Modules</h3>
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
    <span>Page 7 of 15</span>
  </div>
</div>


<!-- ==========================================
     PAGE 8: CODE SNIPPETS - MAIN & MODEL (ALIGNED)
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Implementation - main.dart & model</span>
    <span>Section 7.1 & 7.2</span>
  </div>

  <h2 class="section-title">7. Source Code: Application Root & Data Model</h2>

  <h3 class="sub-title">7.1 Application Root Setup (<code>lib/main.dart</code>)</h3>
  <p>
    The root file wraps the entire widget tree inside a <code>ChangeNotifierProvider</code>, ensuring the <code>TransactionProvider</code> is globally accessible across all screens and widgets.
  </p>

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

  <h3 class="sub-title">7.2 Transaction Model (<code>lib/models/transaction.dart</code>)</h3>
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
    <span>Page 8 of 15</span>
  </div>
</div>


<!-- ==========================================
     PAGE 9: CODE SNIPPETS - PROVIDER (ALIGNED)
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Implementation - TransactionProvider</span>
    <span>Section 7.3</span>
  </div>

  <h2 class="section-title">7.3 State Management Controller (<code>transaction_provider.dart</code>)</h2>
  <p>
    The central state controller managing transaction collections, balance calculations, category grouping, and reactive notifications via <code>notifyListeners()</code>.
  </p>

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
    <span>Page 9 of 15</span>
  </div>
</div>


<!-- ==========================================
     PAGE 10: CODE SNIPPETS - HOME SCREEN (ALIGNED)
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Implementation - HomeScreen</span>
    <span>Section 7.4</span>
  </div>

  <h2 class="section-title">7.4 Responsive Dashboard Screen (<code>home_screen.dart</code>)</h2>
  <p>
    Built using Flutter's <code>CustomScrollView</code> and sliver widgets, delivering smooth 60 FPS performance, reactive Provider binding, and an intuitive empty-state layout.
  </p>

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
    <strong>Sliver Layout Benefit:</strong> <code>SliverList</code> creates visible transaction cards lazily on demand, guaranteeing optimal memory utilization and zero layout jank regardless of ledger size.
  </p>

  <div class="page-footer">
    <span>Vishnu Institute of Technology :: Bhimavaram</span>
    <span>Page 10 of 15</span>
  </div>
</div>


<!-- ==========================================
     PAGE 11: CODE SNIPPETS - ADD TRANSACTION
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Implementation - AddTransactionScreen</span>
    <span>Section 7.5</span>
  </div>

  <h2 class="section-title">7.5 Form Screen & Input Validation (<code>add_transaction_screen.dart</code>)</h2>
  <p>
    Features custom segmented controls for income/expense switching, strict numerical validation, a category dropdown, and calendar date selection.
  </p>

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
    <strong>Form Validation Cycle:</strong> The <code>_formKey.currentState!.validate()</code> call checks all descendant field validators, ensuring invalid or empty transactions cannot corrupt application state.
  </p>

  <div class="page-footer">
    <span>Vishnu Institute of Technology :: Bhimavaram</span>
    <span>Page 11 of 15</span>
  </div>
</div>


<!-- ==========================================
     PAGE 12: CODE SNIPPETS - MODULAR WIDGETS
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Implementation - Modular Widgets</span>
    <span>Section 7.6</span>
  </div>

  <h2 class="section-title">7.6 Source Code: Modular Reusable Widgets</h2>

  <h3 class="sub-title">7.6.1 Balance Card Widget (<code>lib/widgets/balance_card.dart</code>)</h3>
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

  <h3 class="sub-title">7.6.2 Expense Pie Chart Widget (<code>lib/widgets/expense_pie_chart.dart</code>)</h3>
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
    <span>Page 12 of 15</span>
  </div>
</div>


<!-- ==========================================
     PAGE 13: DEPLOYMENT & TESTING MATRIX
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Deployment & Verification Matrix</span>
    <span>Section 8 & 9</span>
  </div>

  <h2 class="section-title">8. Cloud Deployment & System Verification</h2>

  <h3 class="sub-title">8.1 Cloud Deployment Pipeline (GitHub Pages)</h3>
  <p>
    The application is compiled for the Web target using Flutter's high-performance production compiler and published to GitHub Pages:
  </p>
  <pre class="code-box">
<span class="cm"># 1. Compile optimized release build for GitHub Pages subpath</span>
flutter build web --release --base-href "/Expense-Tracker/"

<span class="cm"># 2. Push production artifact to the dedicated gh-pages deployment branch</span>
cd build/web
git init &amp;&amp; git checkout -b gh-pages
git add . &amp;&amp; git commit -m "Deploy Web Build"
git remote add origin https://github.com/Saketh17-max/Expense-Tracker.git
git push -u origin gh-pages --force
  </pre>

  <h3 class="sub-title">8.2 System Testing & Verification Matrix</h3>
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
    <span>Page 13 of 15</span>
  </div>
</div>


<!-- ==========================================
     PAGE 14: OUTPUT SCREENSHOTS & WORKFLOW
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Output Screens & User Workflow</span>
    <span>Section 10</span>
  </div>

  <h2 class="section-title">9. Output Screens & User Workflow Walkthrough</h2>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 6px;">
    <div class="figure-box">
      <img src="{desktop_b64}" class="figure-img" style="height: 135px; width: 100%; object-fit: cover;">
      <div class="caption">Figure 9.1: Desktop Web Dashboard (Live Deployment)</div>
    </div>
    <div class="figure-box">
      <img src="{chart_tx_b64}" class="figure-img" style="height: 135px; width: 100%; object-fit: cover;">
      <div class="caption">Figure 9.2: Category Donut Chart & Transaction Stream</div>
    </div>
    <div class="figure-box">
      <img src="{add_tx_b64}" class="figure-img" style="height: 150px; width: auto; object-fit: contain;">
      <div class="caption">Figure 9.3: New Transaction Form Modal</div>
    </div>
    <div class="figure-box">
      <img src="{dialog_b64}" class="figure-img" style="height: 150px; width: auto; object-fit: contain;">
      <div class="caption">Figure 9.4: Delete Confirmation Dialog</div>
    </div>
  </div>

  <h3 class="sub-title" style="margin-top: 8px;">9.2 User Workflow Step-by-Step</h3>
  <ol style="font-size: 8.5pt;">
    <li><strong>Dashboard Audit:</strong> The user opens the app and immediately sees their financial overview: Total Balance, Income, Expense, and a breakdown chart.</li>
    <li><strong>Initiating New Record:</strong> The user taps the floating <code>+ Add</code> button, opening the <code>AddTransactionScreen</code>.</li>
    <li><strong>Form Input & Validation:</strong> The user toggles between Income and Expense using the <code>SegmentedButton</code>, enters an amount and description, picks a category, selects a date, and presses Save.</li>
    <li><strong>Immediate UI Refresh:</strong> The Provider dispatches the new transaction and runs <code>notifyListeners()</code>, recalculating totals and updating the dashboard instantly.</li>
    <li><strong>Deleting an Entry:</strong> Tapping the trash icon opens a confirmation dialog, safely deleting the item and adjusting the balance once confirmed.</li>
  </ol>

  <div class="page-footer">
    <span>Vishnu Institute of Technology :: Bhimavaram</span>
    <span>Page 14 of 15</span>
  </div>
</div>


<!-- ==========================================
     PAGE 15: CONCLUSION & TECHNICAL SUMMARY (NO VIVA Q&A)
     ========================================== -->
<div class="page">
  <div class="page-header">
    <span>Conclusion & Technical Summary</span>
    <span>Section 11</span>
  </div>

  <h2 class="section-title">10. Project Conclusion & Technical Summary</h2>

  <h3 class="sub-title">10.1 Project Conclusion</h3>
  <p>
    The <strong>Small-Business Income/Expense Tracker</strong> successfully demonstrates how the <strong>Provider</strong> state management architecture provides a robust, predictable, and maintainable framework for cross-platform Flutter applications. By segregating business logic within <code>TransactionProvider</code> and strictly employing reactive listeners (<code>Consumer</code>, <code>context.watch()</code>) and non-listening dispatchers (<code>context.read()</code>), the application achieves high performance, instantaneous arithmetic feedback, and clean separation of concerns.
  </p>

  <h3 class="sub-title">10.2 Technical Summary & Key Achievements</h3>
  <ul>
    <li><strong>Predictable Reactive Architecture:</strong> Implemented pure unidirectional data flow utilizing Flutter's official <code>ChangeNotifier</code> and <code>ChangeNotifierProvider</code>, ensuring state mutates only through dedicated provider methods.</li>
    <li><strong>Live Arithmetic Feedback:</strong> Dynamic recalculation of Total Income, Total Expenses, and Net Balance ($Balance = Income - Expense$) in constant $O(n)$ time complexity, instantly reflected across all active views.</li>
    <li><strong>Categorical Spending Analytics:</strong> Seamless integration with <code>fl_chart</code> to deliver an interactive, visually distinct donut chart that groups business overheads into actionable categories.</li>
    <li><strong>Robust Input Validation:</strong> Strict client-side verification preventing invalid numeric inputs, empty descriptions, or missing categories from entering the financial ledger.</li>
    <li><strong>Cross-Platform Production Deployment:</strong> Verified and deployed across both mobile smartphones and web browsers with automated continuous delivery via GitHub Pages.</li>
  </ul>

  <h3 class="sub-title">10.3 Future Scope & Enhancements</h3>
  <ul>
    <li><strong>Local Offline Persistence:</strong> Integrate lightweight NoSQL storage (such as Hive or SharedPreferences) to cache ledger entries across application restarts.</li>
    <li><strong>Automated PDF Statement Export:</strong> Allow business owners to generate and export monthly profit/loss PDF statements directly from the device.</li>
    <li><strong>Multi-Currency & Tax Handling:</strong> Introduce localized GST/tax calculation options and support for multiple international currencies.</li>
  </ul>

  <h3 class="sub-title" style="margin-top: 10px;">10.4 Official Project Deliverable Links</h3>
  <div class="callout" style="font-size: 8.5pt;">
    &bull; <strong>GitHub Source Code Repository:</strong> <a href="https://github.com/Saketh17-max/Expense-Tracker" style="color:#1d4ed8;">https://github.com/Saketh17-max/Expense-Tracker</a><br>
    &bull; <strong>Live Cloud Web Application:</strong> <a href="https://saketh17-max.github.io/Expense-Tracker/" style="color:#1d4ed8;">https://saketh17-max.github.io/Expense-Tracker/</a>
  </div>

  <div class="page-footer">
    <span>Vishnu Institute of Technology :: Bhimavaram</span>
    <span>Page 15 of 15</span>
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
