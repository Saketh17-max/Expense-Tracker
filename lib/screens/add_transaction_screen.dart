import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/transaction.dart';
import '../providers/transaction_provider.dart';

class AddTransactionScreen extends StatefulWidget {
  const AddTransactionScreen({super.key});

  @override
  State<AddTransactionScreen> createState() => _AddTransactionScreenState();
}

class _AddTransactionScreenState extends State<AddTransactionScreen> {
  // GlobalKey to identify and validate the form
  final _formKey = GlobalKey<FormState>();

  // Controllers to retrieve text from TextFields
  final _titleController = TextEditingController();
  final _amountController = TextEditingController();

  // State variables for dropdown and date picker
  TransactionType? _selectedType;
  DateTime _selectedDate = DateTime.now();

  @override
  void dispose() {
    // Clean up controllers when widget is disposed
    _titleController.dispose();
    _amountController.dispose();
    super.dispose();
  }

  // Method to show Flutter's built-in date picker
  void _presentDatePicker() async {
    final pickedDate = await showDatePicker(
      context: context,
      initialDate: _selectedDate,
      firstDate: DateTime(2020),
      lastDate: DateTime.now(),
    );
    if (pickedDate != null) {
      setState(() {
        _selectedDate = pickedDate;
      });
    }
  }

  // Method to validate and save the transaction
  void _submitData() {
    if (_formKey.currentState!.validate()) {
      final title = _titleController.text;
      final amount = double.tryParse(_amountController.text) ?? 0.0;

      // Type must be selected
      if (_selectedType == null) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text('Please select a transaction type')),
        );
        return;
      }

      // Create new transaction object
      final newTx = TransactionModel(
        id: DateTime.now().toString(),
        title: title,
        amount: amount,
        type: _selectedType!,
        date: _selectedDate,
      );

      // Add transaction using Provider (context.read to avoid listening here)
      context.read<TransactionProvider>().addTransaction(newTx);

      // Show confirmation SnackBar
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Transaction added successfully'),
          backgroundColor: Colors.green,
        ),
      );

      // Return to previous screen
      Navigator.pop(context);
    }
  }

  @override
  Widget build(BuildContext context) {
    // Simple date formatting
    final String formattedDate =
        '${_selectedDate.day.toString().padLeft(2, '0')}-${_selectedDate.month.toString().padLeft(2, '0')}-${_selectedDate.year}';

    return Scaffold(
      appBar: AppBar(
        title: const Text('Add Transaction'),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Card(
          elevation: 4,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(12),
          ),
          child: Padding(
            padding: const EdgeInsets.all(16.0),
            child: Form(
              key: _formKey,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  // Title input
                  TextFormField(
                    controller: _titleController,
                    decoration: const InputDecoration(
                      labelText: 'Transaction Title',
                      hintText: 'e.g. Product Sales, Electricity Bill',
                      border: OutlineInputBorder(),
                    ),
                    validator: (value) {
                      if (value == null || value.trim().isEmpty) {
                        return 'Please enter a transaction title';
                      }
                      return null;
                    },
                  ),
                  const SizedBox(height: 16),
                  
                  // Amount input
                  TextFormField(
                    controller: _amountController,
                    decoration: const InputDecoration(
                      labelText: 'Amount (₹)',
                      hintText: 'e.g. 5000',
                      border: OutlineInputBorder(),
                    ),
                    keyboardType: const TextInputType.numberWithOptions(decimal: true),
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Please enter an amount';
                      }
                      final amount = double.tryParse(value);
                      if (amount == null) {
                        return 'Please enter a valid number';
                      }
                      if (amount <= 0) {
                        return 'Amount must be greater than 0';
                      }
                      return null;
                    },
                  ),
                  const SizedBox(height: 16),
                  
                  // Type dropdown
                  DropdownButtonFormField<TransactionType>(
                    decoration: const InputDecoration(
                      labelText: 'Transaction Type',
                      border: OutlineInputBorder(),
                    ),
                    initialValue: _selectedType,
                    items: const [
                      DropdownMenuItem(
                        value: TransactionType.income,
                        child: Text('Income'),
                      ),
                      DropdownMenuItem(
                        value: TransactionType.expense,
                        child: Text('Expense'),
                      ),
                    ],
                    onChanged: (value) {
                      setState(() {
                        _selectedType = value;
                      });
                    },
                    validator: (value) {
                      if (value == null) {
                        return 'Please select a transaction type';
                      }
                      return null;
                    },
                  ),
                  const SizedBox(height: 16),
                  
                  // Date picker row
                  Row(
                    children: [
                      Expanded(
                        child: Text(
                          'Selected Date: $formattedDate',
                          style: const TextStyle(fontSize: 16),
                        ),
                      ),
                      TextButton(
                        onPressed: _presentDatePicker,
                        child: const Text('Choose Date'),
                      ),
                    ],
                  ),
                  const SizedBox(height: 24),
                  
                  // Submit button
                  ElevatedButton(
                    style: ElevatedButton.styleFrom(
                      padding: const EdgeInsets.symmetric(vertical: 16),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(8),
                      ),
                    ),
                    onPressed: _submitData,
                    child: const Text(
                      'Add Transaction',
                      style: TextStyle(fontSize: 18),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
