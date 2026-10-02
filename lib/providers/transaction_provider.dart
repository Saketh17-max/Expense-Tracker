import 'package:flutter/material.dart';
import '../models/transaction.dart';

class TransactionProvider with ChangeNotifier {
  // The private list of transactions
  final List<TransactionModel> _transactions = [
    // Some initial sample data to show the dashboard
    TransactionModel(
      id: DateTime.now().subtract(const Duration(days: 2)).toString(),
      title: 'Product Sales',
      amount: 5000,
      type: TransactionType.income,
      date: DateTime.now().subtract(const Duration(days: 2)),
    ),
    TransactionModel(
      id: DateTime.now().subtract(const Duration(days: 1)).toString(),
      title: 'Office Supplies',
      amount: 1200,
      type: TransactionType.expense,
      date: DateTime.now().subtract(const Duration(days: 1)),
    ),
  ];

  // Getter to access the transaction list safely
  List<TransactionModel> get transactions {
    // Return a copy or just the list, reversing it to show newest first
    return [..._transactions].reversed.toList();
  }

  // Calculate total income
  double get totalIncome {
    double total = 0;
    for (var tx in _transactions) {
      if (tx.type == TransactionType.income) {
        total += tx.amount;
      }
    }
    return total;
  }

  // Calculate total expense
  double get totalExpense {
    double total = 0;
    for (var tx in _transactions) {
      if (tx.type == TransactionType.expense) {
        total += tx.amount;
      }
    }
    return total;
  }

  // Calculate current balance (Income - Expense)
  double get balance {
    return totalIncome - totalExpense;
  }

  // Add a new transaction
  void addTransaction(TransactionModel newTx) {
    _transactions.add(newTx);
    // notifyListeners() tells all listening widgets (like Consumer) to rebuild
    notifyListeners();
  }

  // Delete a transaction by its ID
  void deleteTransaction(String id) {
    _transactions.removeWhere((tx) => tx.id == id);
    // notifyListeners() updates the UI after deletion
    notifyListeners();
  }
}
