import 'dart:convert';

import 'package:flutter_application_3/models/webtoon.dart';
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

  static Future<WebtoonDetailModel> getWebtoonDetail(String id) async {
    final url = Uri.parse('$baseUrl/$id');
    final response = await http.get(url);
    if (response.statusCode == 200) {
      final Map<String, dynamic> webtoonDetail = jsonDecode(response.body);
      return WebtoonDetailModel.fromJson(webtoonDetail);
    } else {
      throw Exception('Failed to load webtoon detail');
    }
  }

  static Future<List<WebtoonEpisodeModel>> getWebtoonEpisodes(String id) async {
    List<WebtoonEpisodeModel> episodeInstances = [];
    final url = Uri.parse('$baseUrl/$id/episodes');
    final response = await http.get(url);
    if (response.statusCode == 200) {
      final List<dynamic> episodes = jsonDecode(response.body);
      for (var episode in episodes) {
        final ep = WebtoonEpisodeModel.fromJson(episode);
        episodeInstances.add(ep);
      }
      return episodeInstances;
    } else {
      throw Exception('Failed to load webtoon episodes');
    }
  }
}
