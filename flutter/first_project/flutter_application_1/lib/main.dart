import 'package:flutter/material.dart';
import 'package:flutter_application_1/widgets/Button.dart';

void main() {
  runApp(App());
}

// root widget
class App extends StatelessWidget {
  const App({super.key});
  // StatelessWidget : widget without state

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      // MaterialApp : google app style(recommended), CupertinoApp : apple app style
      home: Scaffold(
          // Scaffold : main container
          backgroundColor:
              const Color(0xFF181818), // Color : 0xFF + hex color code
          body: Padding(
            padding: EdgeInsets.symmetric(horizontal: 20), // Padding : padding
            child: Column(
              // Column : vertical layout
              crossAxisAlignment:
                  CrossAxisAlignment.start, // vertical alignment
              children: [
                SizedBox(
                  height: 80,
                ),
                Row(
                  mainAxisAlignment:
                      MainAxisAlignment.end, // horizontal alignment
                  children: [
                    Column(
                      crossAxisAlignment:
                          CrossAxisAlignment.end, // vertical alignment
                      children: [
                        Text('Hey, Tecketing',
                            style: TextStyle(
                              color: Colors.white,
                              fontSize: 28,
                              fontWeight: FontWeight.w800,
                            )),
                        Text('Welcome back',
                            style: TextStyle(
                              // color: Colors.white.withValues(alpha: 0.8), // Define opacity value
                              color: Color.fromRGBO(
                                  255, 255, 255, 0.8), // RGB color with opacity
                              fontSize: 16,
                            )),
                      ],
                    )
                  ],
                ),
                SizedBox(
                  height: 80,
                ),
                Text(
                  'Total Balance',
                  style: TextStyle(
                    color: Color.fromRGBO(255, 255, 255, 1.0),
                    fontSize: 16,
                  ),
                ),
                SizedBox(
                  height: 5,
                ),
                Text(
                  '\$5,194,482',
                  style: TextStyle(
                    color: Color.fromRGBO(255, 255, 255, 1.0),
                    fontSize: 42,
                    fontWeight: FontWeight.w600,
                  ),
                ),
                SizedBox(
                  height: 30,
                ),
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Button(
                        text: "Transfer",
                        bgColor: Colors.amber,
                        textColor: Colors.black),
                    MyButton()
                  ],
                ),
                SizedBox(
                  height: 60,
                ),
                Row(
                  crossAxisAlignment: CrossAxisAlignment.end,
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      'Wallets',
                      style: TextStyle(
                          color: Colors.white,
                          fontSize: 35,
                          fontWeight: FontWeight.w600),
                    ),
                    Text(
                      'View All',
                      style: TextStyle(
                        color: Color.fromRGBO(255, 255, 255, 0.8),
                        fontSize: 18,
                      ),
                    )
                  ],
                ),
                SizedBox(
                  height: 20,
                ),
                Container(
                  clipBehavior: Clip.hardEdge, // hard edge -> prevent overflow
                  decoration: BoxDecoration(
                    color: Color(0xFF1F2123),
                    borderRadius: BorderRadius.circular(25),
                  ),
                  child: Padding(
                    padding: const EdgeInsets.all(30),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              'Euro',
                              style: TextStyle(
                                  color: Colors.white,
                                  fontSize: 32,
                                  fontWeight: FontWeight.w600),
                            ),
                            SizedBox(height: 10),
                            Row(
                              children: [
                                Text(
                                  '6246',
                                  style: TextStyle(
                                      color: Colors.white, fontSize: 20),
                                ),
                                SizedBox(width: 5),
                                Text('EUR',
                                    style: TextStyle(
                                        color:
                                            Color.fromRGBO(255, 255, 255, 0.8),
                                        fontSize: 20)),
                              ],
                            ),
                          ],
                        ),
                        Transform.scale(
                          scale: 2.2,
                          child: Transform.translate(
                            offset: Offset(-8, 15),
                            child: Icon(
                              Icons.euro_rounded,
                              color: Colors.white,
                              size: 88,
                            ),
                          ),
                        )
                      ],
                    ),
                  ),
                ),
              ],
            ),
          )),
    );
  }
}

class MyButton extends StatelessWidget {
  // reusable widget
  // extracted widget
  const MyButton({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: Color(0xFF1F2123),
        borderRadius: BorderRadius.circular(45),
      ),
      child: Padding(
          padding: EdgeInsets.symmetric(horizontal: 50, vertical: 20),
          child: Text('Request',
              style: TextStyle(
                color: Colors.white,
                fontSize: 20,
              ))),
    );
  }
}
