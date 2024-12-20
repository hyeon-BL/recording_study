import 'dart:convert';

import 'package:flutter_application_3/model_model/webtoon.dart';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl =
      'https://webtoon-crawler.nomadcoders.workers.dev';
  static const String today = "today";

  static Future<List<WebtoonModel>> getTodayWebtoons() async {
    // async function -> await until the function is done
    List<WebtoonModel> webtoonInstances = [];
    final url = Uri.parse('$baseUrl/$today');
    final response = await http.get(url); // future에서 response를 받을 때까지 기다림
    if (response.statusCode == 200) {
      // 200: OK
      final List<dynamic> webtoons =
          jsonDecode(response.body); // response.body: json string
      for (var webtoon in webtoons) {
        final toon = WebtoonModel.fromJson(webtoon);
        webtoonInstances.add(toon);
      }
      return webtoonInstances;
    } else {
      throw Exception('Failed to load webtoons');
    }
  }
}
