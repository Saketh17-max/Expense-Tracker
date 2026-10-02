# Small-Business Income/Expense Tracker

## Project Title
Small-Business Income/Expense Tracker

## Problem Statement
Small-business owners need a simple and effective way to monitor their daily financial transactions. Without a clear view of their income and expenses, it is difficult to understand the actual financial status and current balance of the business.

## Objective
To build a clean, mobile-friendly application that allows a small-business owner to easily track income and expenses, view all transactions, and instantly see their total income, total expenses, and current balance through a simple dashboard. 

## Features
- Add new income or expense transactions
- View a dashboard with Total Income, Total Expense, and Current Balance
- View a list of recent transactions
- Delete a transaction with confirmation
- Form validation (prevents empty titles or invalid amounts)
- Date picker to select transaction dates
- Empty state handling when there are no transactions

## Technologies Used
- Flutter
- Dart
- Provider

## Flutter Concepts Used
- **StatelessWidget & StatefulWidget:** Used to build both static UI components and forms that require local state management (like text input and date selection).
- **MaterialApp & Scaffold:** Provided the foundational app structure and Material Design layout.
- **Layouts (Column, Row, Expanded, Padding):** Used to create a responsive and structured UI without overflow errors.
- **ListView.builder:** Used for efficiently displaying the list of transactions.
- **Forms & Validation (TextFormField, Form, DropdownButtonFormField):** Implemented to ensure data integrity before adding a transaction.
- **Navigation (Navigator.push, Navigator.pop):** Used to seamlessly move between the dashboard and the add transaction screen.
- **Dialog & SnackBar:** Used for delete confirmation and success notifications.
- **ThemeData:** Applied to maintain a consistent visual style throughout the app.

## How Provider Works
Provider is a state management solution in Flutter. It allows different widgets to share and react to the same data without passing variables down through every level of the widget tree.
- **ChangeNotifier:** The `TransactionProvider` class extends `ChangeNotifier`. When a transaction is added or deleted, it calls `notifyListeners()`, which signals the UI to update.
- **Consumer / context.watch():** These are used in the UI to listen to the provider. Whenever `notifyListeners()` is called, these widgets rebuild with the latest data.
- **context.read():** Used when we just want to call a method on the provider (like adding or deleting) without needing to listen for UI updates.

## How the Balance Is Calculated
The balance represents the net financial status and is calculated dynamically by subtracting total expenses from total income:
```
Balance = Total Income - Total Expense
```

## SDG Relevance
**SDG 8 – Decent Work and Economic Growth**
This application helps small-business owners effectively monitor their income, expenses, and financial balance. By providing a clear financial overview, it supports better financial management, informed decision-making, and promotes sustainable business growth and economic activity.

## Screenshots
*(Insert Screenshots Below)*

### Screenshot 1: Home Dashboard
![Dashboard Placeholder](screenshot1_dashboard.png)

### Screenshot 2: Add Transaction Form
![Add Transaction Placeholder](screenshot2_add_tx.png)

### Screenshot 3: Transaction List
![Transaction List Placeholder](screenshot3_list.png)

### Screenshot 4: Delete Confirmation
![Delete Confirmation Placeholder](screenshot4_delete.png)

## How to Run

1. Make sure you have Flutter installed.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Run the following commands:

```bash
flutter pub get
flutter run
```
