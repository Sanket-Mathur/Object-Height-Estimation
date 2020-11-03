import 'package:flutter/material.dart';

class Buttons extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              CircleAvatar(
                radius: 30,
                backgroundColor: Colors.blue,
                child: IconButton(
                  icon: Icon(Icons.add_a_photo_outlined),
                  onPressed: () {},
                  color: Colors.white,
                  iconSize: 30,
                ),
              ),
              CircleAvatar(
                radius: 30,
                backgroundColor: Colors.blue,
                child: IconButton(
                  icon: Icon(Icons.add_photo_alternate_outlined),
                  onPressed: () {},
                  color: Colors.white,
                  iconSize: 30,
                ),
              ),
              CircleAvatar(
                radius: 30,
                backgroundColor: Colors.blue,
                child: IconButton(
                  icon: Icon(Icons.cloud_upload_outlined),
                  onPressed: () {},
                  color: Colors.white,
                  iconSize: 30,
                ),
              ),
              CircleAvatar(
                radius: 30,
                backgroundColor: Colors.blue,
                child: IconButton(
                  icon: Icon(Icons.drafts_outlined),
                  onPressed: () {},
                  color: Colors.white,
                  iconSize: 30,
                ),
              ),
            ],
          ),
    );
  }
}
