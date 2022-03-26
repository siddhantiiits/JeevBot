import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:data_table_2/data_table_2.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:nandi_portal/functions.dart';
import 'dart:js' as js;

import 'email_login.dart';

class animalWelfare extends StatefulWidget {
  const animalWelfare({Key? key, required this.user}) : super(key: key);
  final User user;
  @override
  _animalWelfareState createState() => _animalWelfareState();
}

class _animalWelfareState extends State<animalWelfare> {
  final CollectionReference _animalAbuseStream =
      FirebaseFirestore.instance.collection('AnimalWelfare');
  // .where('finalStatus', isEqualTo: true)
  // .snapshots();

  Future<void> updateField(String docID, String fieldName, String fieldValue) {
    return _animalAbuseStream
        .doc(docID)
        .update({fieldName: fieldValue})
        .then((value) => print("User Updated"))
        .catchError((error) => print("Failed to update user: $error"));
  }

  @override
  Widget build(BuildContext context) {
    var status = [
      'Not seen yet',
      'Under Review',
      'Follow Up',
    ];
    print(widget.user);
    // widget.user.updateDisplayName('Pulkit Goyal');
    return StreamBuilder<QuerySnapshot>(
        stream: _animalAbuseStream
            .where('finalStatus', isEqualTo: 'active')
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
              child: drawers(context, 1, widget.user),
            ),
            appBar: AppBar(
              title: const Text(
                "Nandi - Animal Abuse portal",
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
                            label: Text('Description'),
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
                            label: Text('Status'),
                          ),
                          DataColumn(
                            label: Text('Done'),
                          ),
                          DataColumn(
                            label: Text('Remarks'),
                          ),
                        ],
                        // rows: [],
                        rows: List<DataRow>.generate(
                            snapshot.data!.size,
                            (index) => DataRow(cells: [
                                  DataCell(Text((index + 1).toString())),
                                  DataCell(Container(
                                    width: 200,
                                    child: Text(snapshot.data!.docs[index]
                                        ['Image Description']),
                                  )),
                                  DataCell(Text(snapshot
                                      .data!.docs[index]['User Phone Number']
                                      .toString()
                                      .substring(9))),
                                  DataCell(Container(
                                    width: 200,
                                    child: Text(
                                        snapshot.data!.docs[index]['address']),
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
                                    DropdownButton(
                                      value: snapshot.data!.docs[index]
                                          ['status'],
                                      items: status.map((String items) {
                                        return DropdownMenuItem(
                                          value: items,
                                          child: Text(items),
                                        );
                                      }).toList(),
                                      icon:
                                          const Icon(Icons.keyboard_arrow_down),
                                      onChanged: (var newVal) {
                                        updateField(
                                            snapshot.data!.docs[index].id,
                                            'status',
                                            newVal.toString());
                                      },
                                    ),
                                  ),
                                  DataCell(IconButton(
                                      icon: Icon(
                                        Icons.check,
                                        color: Colors.green,
                                      ),
                                      onPressed: () {
                                        showDialog(
                                            context: context,
                                            builder: (BuildContext context) {
                                              return AlertDialog(
                                                  content: const Text(
                                                      "Do you want to permanently mark this as done?"),
                                                  actions: <Widget>[
                                                    TextButton(
                                                      child: const Text(
                                                        "No",
                                                        style: TextStyle(
                                                            color:
                                                                Colors.black),
                                                      ),
                                                      onPressed: () {
                                                        Navigator.of(context)
                                                            .pop();
                                                      },
                                                    ),
                                                    TextButton(
                                                      child: const Text(
                                                        "Yes",
                                                        style: TextStyle(
                                                            color:
                                                                Colors.green),
                                                      ),
                                                      onPressed: () {
                                                        updateField(
                                                            snapshot.data!
                                                                .docs[index].id,
                                                            'finalStatus',
                                                            'inactive');
                                                        Navigator.of(context)
                                                            .pop();
                                                      },
                                                    )
                                                  ]);
                                            });
                                      })),
                                  DataCell(Container(
                                    width: 300,
                                    child: TextField(
                                      controller: TextEditingController(
                                          text: snapshot.data!.docs[index]
                                              ['remarks']),
                                      onSubmitted: (text) {
                                        updateField(
                                                snapshot.data!.docs[index].id,
                                                'remarks',
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

// class showContacts extends StatefulWidget {
//   const showContacts({Key? key}) : super(key: key);
//
//   @override
//   _showContactsState createState() => _showContactsState();
// }
//
// class _showContactsState extends State<showContacts> {
//   bool isLoading = true;
//   var _name1;
//   var _number1;
//   var _docID1;
//   // QuerySnapshot querySnapshot;
//   func() async {
//     QuerySnapshot querySnapshot =
//         await FirebaseFirestore.instance.collection("AnimalWelfare").get();
//     var pinList = List<String>.generate(querySnapshot.docs.length,
//         (i) => querySnapshot.docs[i].get('Pincode').toString());
//     var imgLink = List<String>.generate(querySnapshot.docs.length,
//         (i) => querySnapshot.docs[i].get('Image URL').toString());
//     var numList = List<String>.generate(querySnapshot.docs.length,
//         (i) => "${querySnapshot.docs[i].get('number')}");
//     var docIDlist = List<String>.generate(
//         querySnapshot.docs.length, (i) => "${querySnapshot.docs[i].id}");
//     setState(() {
//       _name1 = nameList;
//       _number1 = numList;
//       _docID1 = docIDlist;
//       isLoading = false;
//     });
//   }
//
//   // final _name = List<String>.generate(10, (i) => "Item $i");
//   void initState() {
//     func();
//     super.initState();
//   }
//
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       // drawer: Drawer(child: drawers(context, 4)),
//       appBar: AppBar(
//         title: Text('ISNB Logistics'),
//         backgroundColor: Colors.cyan,
//         actions: [
//           IconButton(
//             onPressed: () {
//               isLoading = true;
//               func();
//             },
//             icon: Icon(Icons.refresh),
//           )
//         ],
//       ),
//       body: Builder(
//         builder: (context) => Container(
//           child: isLoading
//               ? CircularProgressIndicator()
//               : renderList(_name1, _number1, _docID1, context),
//         ),
//       ),
//     );
//   }
//
//   Widget renderList(var _name, var _num, var _docID, BuildContext ctx) {
//     // print("--------------\n$_name\n$_num\n****");
//     print('Generating Contact List');
//     if (_name.length < 1 || _num.length < 1) {
//       return CircularProgressIndicator();
//     } else {
//       return ListView.builder(
//         itemCount: _name.length,
//         itemBuilder: (context, index) {
//           final String name = _name[index];
//           return ListTile(
//             leading: CircleAvatar(
//               backgroundColor: Colors.black12,
//               child: Icon(
//                 Icons.person,
//                 color: Colors.black,
//                 // size: 40,
//               ),
//             ),
//             title: Text(_name[index]),
//             subtitle: Text(_num[index]),
//             trailing: IconButton(
//               icon: Icon(
//                 Icons.delete_forever,
//                 color: Colors.red,
//               ),
//               onPressed: () {
//                 showDialog(
//                   context: context,
//                   builder: (BuildContext context) {
//                     return AlertDialog(
//                       content:
//                           Text("Do you want to delete \"${_name[index]}\"?"),
//                       actions: <Widget>[
//                         TextButton(
//                           child: Text(
//                             "Cancel",
//                             style: TextStyle(color: Colors.black),
//                           ),
//                           onPressed: () {
//                             Navigator.of(context).pop();
//                           },
//                         ),
//                         TextButton(
//                           child: Text(
//                             "Delete",
//                             style: TextStyle(color: Colors.red),
//                           ),
//                           onPressed: () {
//                             FirebaseFirestore.instance
//                                 .collection("CONTACT-NOS")
//                                 .doc(_docID[index])
//                                 .delete()
//                                 .then((_) {
//                               // Scaffold.of(ctx).showSnackBar(
//                               //   showSnack('Contact deleted Successfully!'),
//                               // );
//                               // Scaffold.of(context).showSnackBar(
//                               //   showSnack('Successfully Deleted!'),
//                               // );
//                               print("success!");
//                             });
//                             setState(() {
//                               _name1.removeAt(index);
//                               _number1.removeAt(index);
//                               _docID1.removeAt(index);
//                             });
//                             Navigator.of(context).pop();
//                           },
//                         ),
//                       ],
//                     );
//                   },
//                 );
//               },
//             ),
//           );
//         },
//       );
//     }
//   }
// }
