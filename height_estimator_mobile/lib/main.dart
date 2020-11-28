import 'package:flutter/material.dart';
import 'package:flutter/painting.dart';

import './Widget/buttons.dart';
import './Models/SelectImage.dart';

List<bool> selectedUnit = [true, false];

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

  callback() {
    setState(() {});
  }

  var unit = 'm';

  void _selectToggle(int index) {
    setState(() {
      for (int i = 0; i < selectedUnit.length; i++) {
        selectedUnit[i] = i == index;
      }
      if (selectedUnit[0]) {
        unit = 'm';
      } else {
        unit = 'ft';
      }
    });
    print(selectedUnit);
  }

  Widget popup(BuildContext ctx) {
    return AlertDialog(
      title: Center(
        child: Text(
            (unit == 'm' ? SelectImage.height : SelectImage.height * 0.305)
                    .toString() +
                ' ' +
                unit),
      ),
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
          Padding(
            padding: EdgeInsets.all(5),
            child: ToggleButtons(
              children: [
                Text('m', style: TextStyle(fontSize: 20)),
                Text('ft', style: TextStyle(fontSize: 20)),
              ],
              isSelected: selectedUnit,
              borderWidth: 5,
              borderRadius: BorderRadius.circular(5),
              color: Colors.white70,
              selectedColor: Colors.white,
              onPressed: (int index) => _selectToggle(index),
            ),
          ),
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
