import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/transaction_provider.dart';
import 'summary_card.dart';

class BalanceCard extends StatelessWidget {
  const BalanceCard({super.key});

  @override
  Widget build(BuildContext context) {
    // We use context.watch() here so that this widget automatically
    // rebuilds whenever the data in TransactionProvider changes.
    final provider = context.watch<TransactionProvider>();

    return Padding(
      padding: const EdgeInsets.all(16.0),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          SummaryCard(
            title: 'Total Income',
            amount: provider.totalIncome,
            color: Colors.green,
          ),
          const SizedBox(width: 8),
          SummaryCard(
            title: 'Total Expense',
            amount: provider.totalExpense,
            color: Colors.red,
          ),
          const SizedBox(width: 8),
          SummaryCard(
            title: 'Balance',
            amount: provider.balance,
            color: Colors.blue,
          ),
        ],
      ),
    );
  }
}
