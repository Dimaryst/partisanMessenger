// import 'dart:html';
// import 'dart:js';
import 'dart:ui';
import 'dart:math';

import 'package:flutter/material.dart';

// Colors {
//   background: #242629 / 0xFF242629
//   message_background: #16161a / 0xFF16161A
//   message_text: #fffffe / 0xFFFFFFFE
//   message_detail: #94a1b2 / 0xFF94A1B2
//   highight_purple: #7f5af0 / 0xFF7F5AF0
//   tertiary: #2cb67d / 0xFF2CB67D
//   error: #f25f4c / 0xFFF25F4C
// }

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          brightness: Brightness.dark,
          backgroundColor: Color(0xFF242629),
          iconTheme:  IconThemeData(color: Color(0xFF2CB67D)),
          leading: IconButton(
            onPressed: (){},
            icon: Icon(
              Icons.menu,
            ),
          ),
          actions: <Widget>[
            IconButton(icon: Icon(Icons.settings), onPressed: (){}),
          ],
        ),
        backgroundColor: Color(0xFF242629),
        body: Stack(
          children:<Widget>[
            Main_Page(),
          ]
        )
      ),
    );
  }
}

class Main_Page extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
    child:Row(
    mainAxisAlignment: MainAxisAlignment.start,
    children:<Widget>[
      Expanded(flex:2, child: Container(child: Contacts()),),
      Expanded(flex:10, child: Container(child: Chat()),), 
    ],
  ),
  );
  }
}

class Text_Message extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container (
      margin: EdgeInsets.fromLTRB(1, 0, 5, 5),
      child: Align(
        alignment: Alignment.bottomRight,
        child: Container(
          decoration: BoxDecoration(
            border: Border.all(
              width: 0.5,
              color: Color(0xFF94A1B2),
              style: BorderStyle.solid
            ),
            borderRadius: BorderRadius.all(Radius.circular(10)),
            boxShadow: [
              BoxShadow(
                color: Color(0xFF94A1B2),
                blurRadius: 1.0,
                spreadRadius: 1.0
              )
            ],
            color: Colors.white
          ),
          padding: EdgeInsets.fromLTRB(10, 0, 10, 0),
          child: TextField(
            textAlign: TextAlign.start,
            obscureText: false,
          )
        ),
      ),
    );
  }
}

dynamic _getContacts([bool append=false]){
  // append ??= false;
  int contactCount = 30;
  if (append) {
    contactCount += 5;
  }
  List arr = [];
  Random rnd = new Random();
  for (int i = 0; i<contactCount; i++) {
    int r = 0 + rnd.nextInt(1000 - 0);
    arr.add(r);
    // print(arr[i]);
  }

  return arr;
}

class Contacts extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    List chat_count = _getContacts();
    // print(chat_count);
    final List<String> items = List<String>.generate(chat_count.length, (index) => 'Chat with id ${chat_count[index]}');
    return Container(
      child: ListView.builder(
        itemCount: items.length,
        itemBuilder: (context, index) {
          return Card(
            child: ListTile(
              title: Text('${items[index]}'),
              leading: Icon(Icons.contact_page),
            )
          );
        },
      ),
    );
  }
}


class Chat extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
    child: Column(
      children: <Widget>[
      Expanded(
        flex: 1,
        child: SingleChildScrollView(
          child: Container(
            decoration: BoxDecoration(
              // color: Colors.blue
            ),
            child: Container(
              child: Column(
                children: [
                  Icon(Icons.text_fields,size:50),
                  Icon(Icons.text_fields,size:50),
                  Icon(Icons.text_fields,size:50),
                  Icon(Icons.text_fields,size:50),
                  Icon(Icons.text_fields,size:50),
                  Icon(Icons.text_fields,size:50),
                  Icon(Icons.text_fields,size:50),
                  Icon(Icons.text_fields,size:50),
                  Icon(Icons.text_fields,size:50),
                  Icon(Icons.text_fields,size:50),
                  Icon(Icons.text_fields,size:50),
                  Icon(Icons.text_fields,size:50),
                  Icon(Icons.text_fields,size:50),
                  Icon(Icons.text_fields,size:50),
                  Icon(Icons.text_fields,size:50),
                ],
              )
            ),
          )
        )
      ),
    Text_Message(),
    ],
    )
    );
  }
}
