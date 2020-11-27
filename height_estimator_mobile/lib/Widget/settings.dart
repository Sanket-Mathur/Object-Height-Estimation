import 'package:flutter/material.dart';

List<bool> _selectedUnit = [true, false];

class Settings extends StatefulWidget {
  static String unit = 'm';

  @override
  _State createState() => _State();
}

class _State extends State<Settings> {

  void _selectToggle(int index) {
    setState(() {
      for (int i = 0; i < _selectedUnit.length; i++) {
        _selectedUnit[i] = i == index;
      }
      if (_selectedUnit[0]) {
        Settings.unit = 'm';
      } else {
        Settings.unit = 'ft';
      }
    });
  }

  List<Map> _sliderParameters = [
    {'parameter': 'HUE Min', 'value': 160},
    {'parameter': 'HUE Max', 'value': 175},
    {'parameter': 'SAT Min', 'value': 175},
    {'parameter': 'SAT Max', 'value': 255},
    {'parameter': 'VAL Min', 'value': 175},
    {'parameter': 'VAL Max', 'value': 255},
    {'parameter': 'Thresh1', 'value': 0},
    {'parameter': 'Thresh2', 'value': 255},
    {'parameter': 'Area Min', 'value': 100},
  ];

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          SizedBox(
            height: 20,
          ),
          Text(
            'Settings',
            textScaleFactor: 2,
          ),
          SizedBox(
            height: 20,
          ),
          ToggleButtons(
            children: [
              Text('m', style: TextStyle(fontSize: 20)),
              Text('ft', style: TextStyle(fontSize: 20)),
            ],
            isSelected: _selectedUnit,
            onPressed: (int index) => _selectToggle(index),
          ),
          SizedBox(
            height: 10,
          ),
          for (Map item in _sliderParameters)
            Container(
              child: Row(
                children: [
                  Flexible(
                    flex: 2,
                    child: Center(
                      child: Text(
                        item['parameter'],
                        style: TextStyle(fontSize: 15),
                      ),
                    ),
                  ),
                  Flexible(
                    flex: 8,
                    child: Slider(
                        value: item['value'].toDouble(),
                        min: 0,
                        max: 255,
                        divisions: 51,
                        label: '${item['value']}',
                        onChanged: (double value) {
                          setState(() {
                            item['value'] = value;
                          });
                        }),
                  ),
                ],
              ),
            ),
          Container(
            height: 150,
            child: Image.asset('assets/images/placeholder.png'),
          ),
          // Placeholder for the images that will go here
        ],
      ),
    );
  }
}
