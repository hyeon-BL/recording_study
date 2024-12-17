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
        backgroundColor: Color(0xFF181818), // Color : 0xFF + hex color code
        body: Padding(padding: EdgeInsets.symmetric(horizontal: 40), // Padding : padding
          child: Column( // Column : vertical layout
          children: [
            SizedBox(
              height: 80,
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.end, // horizontal alignment
              children: [
                Column(
                  crossAxisAlignment: CrossAxisAlignment.end, // vertical alignment
                  children: [
                    Text('Hey, Tecketing',
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 28,
                        fontWeight: FontWeight.w800,
                      )),
                    Text('Welcome back',
                      style: TextStyle(
                        color: Colors.white.withValues(alpha: 0.8), // Define opacity value
                        fontSize: 16,
                      )),
                  ],
                )
              ],
            )
          ],
        ),
      )
      ),
    );
  }
}