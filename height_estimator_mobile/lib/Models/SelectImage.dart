import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:convert';

class SelectImage {
  static var _image;

  static Widget displayImage() {
    return _image==null ? Image.asset('assets/images/imgPH.png') : Image.file(_image);
  }

  void selectGallery(Function cb) async {
    _image = await ImagePicker.pickImage(
      source: ImageSource.gallery,
    );
    List<int> imageBytes = _image.readAsBytesSync();
    String base64Image = base64Encode(imageBytes);
    print(base64Image);
    cb();
  }

  void selectCamera(Function cb) async {
    _image = await ImagePicker.pickImage(
      source: ImageSource.camera,
    );
    List<int> imageBytes = _image.readAsBytesSync();
    String base64Image = base64Encode(imageBytes);
    print(base64Image);
    cb();
  }
}
