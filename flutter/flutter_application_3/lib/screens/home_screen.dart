import 'package:flutter/material.dart';
import 'package:flutter_application_3/model_model/webtoon.dart';
import 'package:flutter_application_3/services/api_service.dart';
import 'package:flutter_application_3/widgets/webtoon_widget.dart';

class HomeScreen extends StatelessWidget {
  HomeScreen({super.key});

  final Future<List<WebtoonModel>> webtoons = ApiService.getTodayWebtoons();

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
                return Column(
                  children: [
                    SizedBox(height: 50),
                    Expanded(child: makeList(snapshot)),
                  ],
                );
              }
              return const Center(
                child: CircularProgressIndicator(),
              );
            }));
  }

  ListView makeList(AsyncSnapshot<List<WebtoonModel>> snapshot) {
    return ListView.separated(
        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
        // ListView: 스크롤 가능한 리스트(builder: 동적인 리스트 생성)
        itemBuilder: (context, index) {
          print(index);
          var webtoon = snapshot.data![index];
          return Webtoon(
            title: webtoon.title,
            thumb: webtoon.thumb,
            id: webtoon.id,
          );
        },
        separatorBuilder: (context, index) => SizedBox(width: 40),
        // separatorBuilder: 리스트의 각 요소 사이에 구분선을 추가
        scrollDirection: Axis.horizontal,
        itemCount: snapshot.data!.length);
  }
}
