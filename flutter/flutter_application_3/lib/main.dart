import 'package:flutter/material.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp(
      {super.key}); // key is a property of the widget to uniquely identify it

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: HomeScreen(),
    );
  }
}
