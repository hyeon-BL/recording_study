import 'dart:async';
import 'package:flutter/material.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  static const twentyFiveMinutes = 1500;
  int totalSeconds = 15;
  bool isRunning = false;
  int pomodoros = 0;
  late Timer timer;

  void onTick(Timer timer) {
    setState(() {
      if (totalSeconds > 0) {
        totalSeconds--;
      } else {
        setState(() {
          timer.cancel();
          pomodoros++;
          isRunning = !isRunning;
          totalSeconds = twentyFiveMinutes;
        });
      }
    });
  }

  void onStartpressed() {
    // duration 마다 timer function을 실행(함수에 괄호를 넣지 않음, 괄호는 즉시 실행 의미)
    timer = Timer.periodic(const Duration(seconds: 1), (onTick));
    setState(() {
      isRunning = !isRunning;
    });
  }

  void onStoppressed() {
    timer.cancel();
    setState(() {
      isRunning = !isRunning;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Theme.of(context).scaffoldBackgroundColor,
      body: Column(
        children: [
          Flexible(
            flex: 1, // ratio of 1:1
            child: Container(
              alignment: Alignment.bottomCenter,
              child: Text('$totalSeconds',
                  style: TextStyle(
                      color: Theme.of(context).cardColor,
                      fontSize: 89,
                      fontWeight: FontWeight.w900)),
            ),
          ),
          Flexible(
            flex: 3, // ratio of 1:2
            child: Center(
              child: IconButton(
                iconSize: 120,
                color: Theme.of(context).cardColor,
                onPressed: isRunning ? onStoppressed : onStartpressed,
                icon: Icon(isRunning
                    ? Icons.pause_circle_outline
                    : Icons.play_circle_outline),
              ),
            ),
          ),
          Flexible(
            flex: 1, // ratio of 1:1
            child: Row(
              children: [
                Expanded(
                  child: Container(
                    decoration: BoxDecoration(
                      color: Theme.of(context).cardColor,
                      borderRadius: BorderRadius.only(
                        topLeft: Radius.circular(30),
                        topRight: Radius.circular(30),
                      ),
                    ),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Text(
                          'Pomodoros',
                          style: TextStyle(
                              fontSize: 20,
                              fontWeight: FontWeight.w700,
                              color: Theme.of(context)
                                  .textTheme
                                  .headlineLarge!
                                  .color),
                        ),
                        Text(
                          '$pomodoros',
                          style: TextStyle(
                              fontSize: 40,
                              fontWeight: FontWeight.w900,
                              color: Theme.of(context)
                                  .textTheme
                                  .headlineLarge!
                                  .color),
                        ),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
