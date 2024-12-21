class WebtoonModel {
  late final String title, thumb, id;

  WebtoonModel.fromJson(Map<String, dynamic> json) // json: Map<String, dynamic>
      : title = json['title'],
        thumb = json['thumb'],
        id = json['id'];
}

class WebtoonDetailModel {
  final String title, about, genre, age;

  WebtoonDetailModel.fromJson(Map<String, dynamic> json)
      : title = json['title'],
        about = json['about'],
        genre = json['genre'],
        age = json['age'];
}

class WebtoonEpisodeModel {
  final String id, title, rating, date;

  WebtoonEpisodeModel.fromJson(Map<String, dynamic> json)
      : id = json['id'],
        title = json['title'],
        rating = json['rating'],
        date = json['date'];
}
