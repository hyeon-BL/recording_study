import 'package:flutter/material.dart';

void main() {
  runApp(const MainApp());
}

class MainApp extends StatefulWidget {
  // App
  const MainApp({super.key});

  @override
  State<MainApp> createState() => _MainAppState();
}

class _MainAppState extends State<MainApp> {
  // store widget data and ui state
  List<int> numbers = [];

  void OnClick() {
    // update the state of the app
    setState(() {
      // data is new, so we need to update the UI(rerun build method)
      numbers.add(numbers.length + 1);
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Color(0xFFF4EDDB),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                'Click Count',
                style: TextStyle(fontSize: 30),
              ),
              for (var number in numbers)
                Text(
                  number.toString(),
                  style: TextStyle(fontSize: 30),
                ),
              IconButton(
                  // onPressed is a function that will be called when the button is clicked
                  onPressed: OnClick,
                  icon: const Icon(Icons.add_box_rounded)),
            ],
          ),
        ),
      ),
    );
  }
}
