import 'package:flutter/material.dart';
import 'package:fl_chart/fl_chart.dart';
import 'package:provider/provider.dart';
import '../providers/transaction_provider.dart';

class ExpensePieChart extends StatelessWidget {
  const ExpensePieChart({super.key});

  @override
  Widget build(BuildContext context) {
    final provider = context.watch<TransactionProvider>();
    final expensesByCategory = provider.expensesByCategory;

    if (expensesByCategory.isEmpty) {
      return const SizedBox(
        height: 200,
        child: Center(
          child: Text(
            'No expenses to show in chart',
            style: TextStyle(color: Colors.grey),
          ),
        ),
      );
    }

    // Assign colors to categories
    final Map<String, Color> categoryColors = {
      'Food': Colors.orange,
      'Transport': Colors.blue,
      'Utilities': Colors.cyan,
      'Supplies': Colors.purple,
      'Other': Colors.grey,
    };

    List<PieChartSectionData> sections = expensesByCategory.entries.map((entry) {
      final category = entry.key;
      final amount = entry.value;
      final color = categoryColors[category] ?? Colors.indigo;

      return PieChartSectionData(
        color: color,
        value: amount,
        title: '₹${amount.toInt()}',
        radius: 50,
        titleStyle: const TextStyle(
          fontSize: 12,
          fontWeight: FontWeight.bold,
          color: Colors.white,
        ),
      );
    }).toList();

    return Column(
      children: [
        const Text(
          'Expenses by Category',
          style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
        ),
        const SizedBox(height: 16),
        SizedBox(
          height: 200,
          child: PieChart(
            PieChartData(
              sections: sections,
              centerSpaceRadius: 40,
              sectionsSpace: 2,
            ),
          ),
        ),
        const SizedBox(height: 16),
        // Legend
        Wrap(
          spacing: 16,
          runSpacing: 8,
          alignment: WrapAlignment.center,
          children: expensesByCategory.keys.map((category) {
            return Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                Container(
                  width: 12,
                  height: 12,
                  decoration: BoxDecoration(
                    color: categoryColors[category] ?? Colors.indigo,
                    shape: BoxShape.circle,
                  ),
                ),
                const SizedBox(width: 4),
                Text(category, style: const TextStyle(fontSize: 12)),
              ],
            );
          }).toList(),
        ),
      ],
    );
  }
}
