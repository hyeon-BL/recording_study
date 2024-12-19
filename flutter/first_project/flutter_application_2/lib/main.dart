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
  bool showTitle = true;
  // store widget data and ui state
  List<int> numbers = [];

  void toggletitle() {
    setState(() {
      showTitle = !showTitle;
    });
  }

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
      theme: ThemeData(
        textTheme: TextTheme(
          titleLarge: TextStyle(color: Colors.red),
        ),
      ),
      home: Scaffold(
        backgroundColor: Color(0xFFF4EDDB),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              showTitle ? MyLargeTitle() : Text('No Title'),
              ElevatedButton(
                onPressed: toggletitle,
                child: Text('Toggle Title'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class MyLargeTitle extends StatefulWidget {
  // seqarate widget -> don't apply state
  const MyLargeTitle({
    super.key,
  });

  @override
  State<MyLargeTitle> createState() => _MyLargeTitleState();
}

class _MyLargeTitleState extends State<MyLargeTitle> {
  int count = 0;

  // init state(initialize) -> build -> dispose(delete widget tree)
  @override
  void initState() {
    // called only once
    super.initState();
    print('initState');
    count = 0;
  }

  @override
  void dispose() {
    // dispose the resources
    super.dispose();
    print('dispose');
  }

  @override
  Widget build(BuildContext context) {
    print('build');
    // context has the information about the parents widget
    return Text(
      'My Large Title',
      style: TextStyle(
          fontSize: 30, color: Theme.of(context).textTheme.titleLarge?.color),
    );
  }
}
