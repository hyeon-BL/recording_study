import 'package:flutter/material.dart';

void main() {
  runApp(App());
}

// root widget
class App extends StatelessWidget{ // StatelessWidget : widget without state
  
  @override
  Widget build(BuildContext context) {
    return MaterialApp( // MaterialApp : google app style(recommended), CupertinoApp : apple app style
      home: Scaffold( // Scaffold : main container
        appBar: AppBar( // AppBar : top bar
          title: Text('Hello World'), // Text : text widget
        ),
        body: Center( // Center : center align
          child: Text('Hello World'), // Text : text widget
        ),
      ),
    );
  }
}