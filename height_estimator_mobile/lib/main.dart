import 'package:flutter/material.dart';
import 'package:flutter/painting.dart';

import './Widget/buttons.dart';
import './Widget/settings.dart';
import './Models/SelectImage.dart';

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
          child: Buttons(callback),
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

  callback() {
    setState(() {});
  }

  Widget popup(BuildContext ctx) {
    return AlertDialog(
      title: Center(
          child: Text((Settings.unit == 'm'
                      ? SelectImage.height
                      : SelectImage.height * 0.305)
                  .toString() +
              ' ' +
              Settings.unit)),
      actions: [
        FlatButton(
          onPressed: () {
            Navigator.of(ctx).pop();
          },
          child: Icon(Icons.check),
        ),
      ],
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
      body: Column(
        mainAxisAlignment: MainAxisAlignment.end,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Expanded(
            child: Center(
              child: SelectImage.displayImage(),
            ),
          ),
          Padding(
            padding: EdgeInsets.all(25),
            child: RaisedButton(
              // onPressed: getRes,
              onPressed: SelectImage.found
                  ? () {
                      showDialog(
                          context: context,
                          builder: (BuildContext ctx) => popup(ctx));
                    }
                  : null,
              color: Colors.blue,
              child: Text(
                'Estimate',
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 20,
                ),
              ),
            ),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.add),
        onPressed: () => _showInputButtons(context),
      ),
    );
  }
}
