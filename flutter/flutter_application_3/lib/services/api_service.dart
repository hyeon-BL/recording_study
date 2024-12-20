import 'package:http/http.dart' as http;

class ApiService {
  final String baseUrl = 'https://webtoon-crawler.nomadcoders.workers.dev';
  final String today = "today";

  void getTodayWebtoons() async {
    // async function -> await until the function is done
    final url = Uri.parse('$baseUrl/$today');
    final response = await http.get(url); // future에서 response를 받을 때까지 기다림
    if (response.statusCode == 200) {
      print(response.body);
    } else {
      throw Exception('Failed to load webtoons');
    }
  }
}
