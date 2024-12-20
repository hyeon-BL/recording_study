import 'package:flutter/material.dart';
import 'package:flutter_application_3/model_model/webtoon.dart';
import 'package:flutter_application_3/services/api_service.dart';

class HomeScreen extends StatelessWidget {
  HomeScreen({super.key});

  Future<List<WebtoonModel>> webtoons = ApiService.getTodayWebtoons();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,
        appBar: AppBar(
          elevation: 1,
          shadowColor: Colors.grey[100],
          backgroundColor: Colors.white,
          foregroundColor: Colors.green,
          title: const Center(
            child: Text(
              '오늘의 웹툰',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.w600),
            ),
          ),
        ),
        body: FutureBuilder(
            // 기다림 상태를 보여주는 위젯
            future: webtoons,
            builder: (context, snapshot) {
              // snapshot: future의 결과를 가지고 있음
              if (snapshot.hasData) {
                return const Text('Data is loaded');
              }
              return const Center(
                child: CircularProgressIndicator(),
              );
            }));
  }
}
