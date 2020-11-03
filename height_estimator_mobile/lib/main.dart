import 'package:flutter/material.dart';

import './Widget/buttons.dart';
import './Widget/settings.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Height Estimator',
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  void _showInputButtons(BuildContext ctx) {
    showModalBottomSheet(
      context: ctx,
      builder: (_) {
        return Container(
          height: 100,
          child: Buttons(),
        );
      },
    );
  }

  void _showSettings(BuildContext ctx) {
    showModalBottomSheet(
      isScrollControlled: true,
      context: ctx,
      builder: (_) {
        return Settings();
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Height Estimator'),
        actions: [
          IconButton(
            icon: Icon(Icons.settings_sharp),
            onPressed: () => _showSettings(context),
          )
        ],
      ),
      body: Center(
        child: Text('No Image Selected'),
      ),
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.add),
        onPressed: () => _showInputButtons(context),
      ),
    );
  }
}