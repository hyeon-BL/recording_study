class WebtoonModel {
  late final String title, thumb, id;

  WebtoonModel.fromJson(Map<String, dynamic> json) // json: Map<String, dynamic>
      : title = json['title'],
        thumb = json['thumb'],
        id = json['id'];
}
