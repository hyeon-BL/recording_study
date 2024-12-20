import 'package:flutter/material.dart';
import 'package:flutter_application_3/services/api_service.dart';
import 'screens/home_screen.dart';

void main() {
  ApiService().getTodayWebtoons();
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
