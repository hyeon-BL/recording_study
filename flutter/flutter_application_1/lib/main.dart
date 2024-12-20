import 'package:flutter/material.dart';
import 'package:flutter_application_1/widgets/Button.dart';
import 'package:flutter_application_1/widgets/currency_card.dart';

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
          body: SingleChildScrollView(
            // SingleChildScrollView : scrollable container
            child: Padding(
              padding:
                  EdgeInsets.symmetric(horizontal: 20), // Padding : padding
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
                                color: Color.fromRGBO(255, 255, 255,
                                    0.8), // RGB color with opacity
                                fontSize: 16,
                              )),
                        ],
                      )
                    ],
                  ),
                  SizedBox(
                    height: 40,
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
                  CurrencyCard(
                    name: 'Euro',
                    code: 'EUR',
                    amount: '6 428',
                    icon: Icons.euro_rounded,
                    isInverted: false,
                    order: 0,
                  ),
                  CurrencyCard(
                    name: 'Dollar',
                    code: 'USD',
                    amount: '5 153',
                    icon: Icons.attach_money_rounded,
                    isInverted: true,
                    order: 1,
                  ),
                  CurrencyCard(
                    name: 'Pound',
                    code: 'GBP',
                    amount: '4 428',
                    icon: Icons.money_rounded,
                    isInverted: false,
                    order: 2,
                  ),
                ],
              ),
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
