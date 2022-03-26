import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'dart:js' as js;
import 'package:audioplayers/audioplayers.dart';

import 'email_login.dart';
import 'functions.dart';

class DiseaseReporting extends StatefulWidget {
  const DiseaseReporting({Key? key, required this.user}) : super(key: key);
  final User user;

  @override
  _DiseaseReportingState createState() => _DiseaseReportingState();
}

class _DiseaseReportingState extends State<DiseaseReporting> {
  final CollectionReference _diseaseReportingStream =
      FirebaseFirestore.instance.collection('Disease Reporting');
  AudioPlayer audioPlayer = AudioPlayer();

  Future<void> updateField(String docID, String fieldName, String fieldValue) {
    return _diseaseReportingStream
        .doc(docID)
        .update({fieldName: fieldValue})
        .then((value) => print("User Updated"))
        .catchError((error) => print("Failed to update user: $error"));
  }

  play(String url) async {
    int result = await audioPlayer.play(url);
    if (result == 1) {
      print("sound played successfully");
    }

    //   player.onAudioPositionChanged.listen((Duration  p) => {
    //   print('Current position: $p');
    //       setState(() => position = p);
    // });
  }

  @override
  Widget build(BuildContext context) {
    return StreamBuilder<QuerySnapshot>(
        stream: _diseaseReportingStream
            // .where('finalStatus', isEqualTo: 'active')
            .snapshots(includeMetadataChanges: true),
        builder: (BuildContext context, AsyncSnapshot<QuerySnapshot> snapshot) {
          if (snapshot.hasError) {
            print('Something went wrong');
          }
          if (snapshot.connectionState == ConnectionState.waiting) {
            print("Loading Animal Abuse data");
            print(snapshot.hasData);
          }
          return Scaffold(
            drawer: Drawer(
              child: drawers(context, 2, widget.user),
            ),
            appBar: AppBar(
              title: const Text(
                "Nandi - Disease Reporting portal",
                // style: TextStyle(color: Colors.white),
              ),
              backgroundColor: Colors.cyan,
              actions: <Widget>[
                IconButton(
                  icon: Icon(
                    Icons.exit_to_app,
                    // color: Colors.white,
                  ),
                  onPressed: () {
                    FirebaseAuth auth = FirebaseAuth.instance;
                    auth.signOut().then((res) {
                      Navigator.pushAndRemoveUntil(
                          context,
                          MaterialPageRoute(builder: (context) => EmailLogIn()),
                          (Route<dynamic> route) => false);
                    });
                  },
                )
              ],
            ),
            body: Padding(
              padding: const EdgeInsets.all(8),
              child: SingleChildScrollView(
                scrollDirection: Axis.horizontal,
                child: snapshot.hasData
                    ? DataTable(
                        dataRowHeight: 50,
                        // columnSpacing: 12,
                        // horizontalMargin: 12,
                        // minWidth: 600,
                        columns: const [
                          DataColumn(
                            label: Text('S. No.'),
                          ),
                          DataColumn(
                            label: Text('Name'),
                          ),
                          DataColumn(
                            label: Text('Contact Number'),
                          ),
                          DataColumn(
                            label: Text('Location'),
                          ),
                          DataColumn(
                            label: Text('Link'),
                          ),
                          DataColumn(
                            label: Text('Symptoms'),
                          ),
                          DataColumn(
                            label: Text('Disease Detected'),
                          ),
                        ],
                        // rows: [],
                        rows: List<DataRow>.generate(
                            snapshot.data!.size,
                            (index) => DataRow(cells: [
                                  DataCell(Text((index + 1).toString())),
                                  DataCell(Container(
                                    width: 100,
                                    child: Text(
                                        snapshot.data!.docs[index]['Name']),
                                  )),
                                  DataCell(Text(snapshot
                                      .data!.docs[index]['User Phone Number']
                                      .toString()
                                      .substring(9))),
                                  DataCell(SizedBox(
                                    // width: 200,
                                    child: Text(
                                        snapshot.data!.docs[index]['pincode']),
                                  )),
                                  DataCell(TextButton(
                                    onPressed: () {
                                      js.context.callMethod('open', [
                                        snapshot.data!.docs[index]['Image URL']
                                      ]);
                                    },
                                    child: const Text('Open Image/Video'),
                                  )),

                                  DataCell(
                                    snapshot.data!.docs[index]['Symptoms']
                                                .toString()
                                                .substring(0, 8) !=
                                            "https://"
                                        ? Text(snapshot.data!.docs[index]
                                            ['Symptoms'])
                                        : TextButton.icon(
                                            onPressed: () {
                                              play(snapshot.data!.docs[index]
                                                  ['Symptoms']);
                                            },
                                            icon: Icon(Icons.play_arrow),
                                            label: Text(
                                              "Play Sound",
                                              style: TextStyle(
                                                  color: Colors.black),
                                            ),
                                          ),
                                  ),
                                  DataCell(Container(
                                    width: 300,
                                    child: TextField(
                                      decoration: InputDecoration(
                                          hintText: snapshot.data!.docs[index]
                                              ['detected_disease']),
                                      controller: TextEditingController(
                                          // text: snapshot.data!.docs[index]
                                          //     ['detected_disease'],
                                          ),
                                      onSubmitted: (text) {
                                        updateField(
                                                snapshot.data!.docs[index].id,
                                                'detected_disease',
                                                text)
                                            .then((vaklue) =>
                                                print('Remarks updated'));
                                      },
                                    ),
                                  )),

                                  // DataCell(Text(index.toString())),
                                  // DataCell(Text(index.toString())),
                                ])),
                      )
                    : CircularProgressIndicator(),
              ),
            ),
          );
        });
  }
}
