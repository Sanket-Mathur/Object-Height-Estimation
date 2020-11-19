import 'package:http/http.dart' as http;
import 'dart:convert';

Future identifyStandard(Map<String, String> data) async{
  http.Response response = await http.post(
    'http://10.0.2.2:5000/api',
    headers: {"Content-Type": "application/json"},
    body: json.encode(data),
  );
  return response.body;
}