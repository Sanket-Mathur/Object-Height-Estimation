import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:convert';

import '../API/api.dart';

class SelectImage {
  static var _image;
  static bool found = false;

  static Widget displayImage() {
    return _image == null
        ? Image.asset('assets/images/imgPH.png')
        : Image.file(_image);
  }

  void selectGallery(Function cb) async {
    _image = await ImagePicker.pickImage(
      source: ImageSource.gallery,
    );
    List<int> imageBytes = _image.readAsBytesSync();
    String base64Image = base64Encode(imageBytes);
    final result = await identifyStandard({
      "image": base64Image,
    });
    var decodedData = jsonDecode(result);
    if (decodedData['found'] == 'yes') {
      List<int> img64 = base64Decode(decodedData['img']);
      _image.writeAsBytesSync(img64);
      found = true;
    } else {
      print('Not Found');
      found = false;
    }
    cb();
  }

  void selectCamera(Function cb) async {
    _image = await ImagePicker.pickImage(
      source: ImageSource.camera,
    );
    List<int> imageBytes = _image.readAsBytesSync();
    String base64Image = base64Encode(imageBytes);
    final result = await identifyStandard({
      "image": base64Image,
    });
    var decodedData = jsonDecode(result);
    if (decodedData['found'] == 'yes') {
      List<int> img64 = base64Decode(decodedData['img']);
      _image.writeAsBytesSync(img64);
      found = true;
    } else {
      print('Not Found');
      found = false;
    }
    cb();
  }
}
