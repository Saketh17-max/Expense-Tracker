import 'package:flutter/material.dart';
import '../models/transaction.dart';

class TransactionProvider with ChangeNotifier {
  // Private list of transactions
  final List<TransactionModel> _transactions = [
    TransactionModel(
      id: DateTime.now().subtract(const Duration(days: 2)).toString(),
      title: 'Product Sales',
      amount: 5000,
      type: TransactionType.income,
      date: DateTime.now().subtract(const Duration(days: 2)),
      category: 'Sales',
    ),
    TransactionModel(
      id: DateTime.now().subtract(const Duration(days: 1)).toString(),
      title: 'Office Supplies',
      amount: 1200,
      type: TransactionType.expense,
      date: DateTime.now().subtract(const Duration(days: 1)),
      category: 'Supplies',
    ),
    TransactionModel(
      id: DateTime.now().subtract(const Duration(days: 3)).toString(),
      title: 'Electricity Bill',
      amount: 800,
      type: TransactionType.expense,
      date: DateTime.now().subtract(const Duration(days: 3)),
      category: 'Utilities',
    ),
  ];

  List<TransactionModel> get transactions {
    return [..._transactions].reversed.toList();
  }

  double get totalIncome {
    double total = 0;
    for (var tx in _transactions) {
      if (tx.type == TransactionType.income) total += tx.amount;
    }
    return total;
  }

  double get totalExpense {
    double total = 0;
    for (var tx in _transactions) {
      if (tx.type == TransactionType.expense) total += tx.amount;
    }
    return total;
  }

  double get balance => totalIncome - totalExpense;

  // Group expenses by category for charts
  Map<String, double> get expensesByCategory {
    Map<String, double> groupedData = {};
    for (var tx in _transactions) {
      if (tx.type == TransactionType.expense) {
        if (groupedData.containsKey(tx.category)) {
          groupedData[tx.category] = groupedData[tx.category]! + tx.amount;
        } else {
          groupedData[tx.category] = tx.amount;
        }
      }
    }
    return groupedData;
  }

  // Group income by category for charts
  Map<String, double> get incomeByCategory {
    Map<String, double> groupedData = {};
    for (var tx in _transactions) {
      if (tx.type == TransactionType.income) {
        if (groupedData.containsKey(tx.category)) {
          groupedData[tx.category] = groupedData[tx.category]! + tx.amount;
        } else {
          groupedData[tx.category] = tx.amount;
        }
      }
    }
    return groupedData;
  }

  void addTransaction(TransactionModel newTx) {
    _transactions.add(newTx);
    notifyListeners();
  }

  void deleteTransaction(String id) {
    _transactions.removeWhere((tx) => tx.id == id);
    notifyListeners();
  }
}
