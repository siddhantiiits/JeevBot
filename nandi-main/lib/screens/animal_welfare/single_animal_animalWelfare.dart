import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:nandi/utils/RoundedButton.dart';
import 'package:nandi/utils/RoundedButton1.dart';
import 'package:sizer/sizer.dart';
import 'package:url_launcher/url_launcher.dart';

import '../../constants.dart';

class SingleAnimalPage extends StatefulWidget {
  var data;

  SingleAnimalPage({required this.data});

  @override
  _SingleAnimalPageState createState() => _SingleAnimalPageState();
}

class _SingleAnimalPageState extends State<SingleAnimalPage> {
  String dropdownValue = "Not seen yet";
  late TextEditingController remarkController;
  Color color = Colors.grey;

  Future<void> updateField(String docID, String fieldName, String fieldValue) {
    return FirebaseFirestore.instance
        .collection('AnimalWelfare')
        .doc(docID)
        .update({fieldName: fieldValue})
        .then((value) => print("User Updated"))
        .catchError((error) => print("Failed to update user: $error"));
  }

  Future<void>? _launched;

  Future<void> _launchInBrowser(String url) async {
    if (!await launch(
      url,
      forceSafariVC: false,
      forceWebView: false,
      headers: <String, String>{'my_header_key': 'my_header_value'},
    )) {
      throw 'Could not launch $url';
    }
  }

  void pushRemark() async {
    if (remarkController.value.text.isNotEmpty) {
      await FirebaseFirestore.instance
          .collection('AnimalWelfare')
          .doc(widget.data.id)
          .update({'remarks': remarkController.value.text});
      var snackBar = SnackBar(
        backgroundColor: Colors.blue,
        content: Text("Remark updated successfully"),
      );
      ScaffoldMessenger.of(context).showSnackBar(snackBar);
    } else {
      var snackBar = SnackBar(
        backgroundColor: Colors.red,
        content: Text("Please enter a remark to update"),
      );
      ScaffoldMessenger.of(context).showSnackBar(snackBar);
    }
  }

  @override
  void initState() {
    remarkController = TextEditingController(text: widget.data['remarks']);
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: Stack(
        children: [
          Container(
            width: 100.w,
            height: 45.h,
            child: Hero(
              tag: widget.data["Image URL"],
              child: Image.network(
                widget.data["Image URL"],
                fit: BoxFit.cover,
              ),
            ),
          ),
          Padding(
            padding: EdgeInsets.only(top: 40.h),
            child: Container(
              height: 100.h,
              padding: EdgeInsets.only(left: 2.w, right: 2.w, top: 6.h),
              width: 100.w,
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.only(
                  topLeft: Radius.circular(10.w),
                  topRight: Radius.circular(10.w),
                ),
              ),
              child: SingleChildScrollView(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceAround,
                  children: [
                    Container(
                      height: 10.h,
                      child: Text(
                        widget.data["Image Description"]
                            .toString()
                            .toUpperCase(),
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          fontSize: 20.sp,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                    SizedBox(
                      height: 2.h,
                    ),
                    Container(
                      width: 100.w,
                      child: Center(
                        child: Text(
                          widget.data["address"],
                          style: TextStyle(
                            fontSize: 12.sp,
                          ),
                        ),
                      ),
                    ),
                    SizedBox(
                      height: 6,
                    ),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceAround,
                      children: [
                        Text(
                          widget.data["User Phone Number"],
                          style: TextStyle(
                            fontSize: 12.sp,
                          ),
                        ),
                        Container(
                          width: 35.w,
                          child: DropdownButton<String>(
                            icon: const Icon(Icons.arrow_drop_down),
                            hint: Text(dropdownValue),
                            iconSize: 24,
                            elevation: 16,
                            style: const TextStyle(color: Colors.black),
                            underline: Container(
                              height: 2,
                              color: Colors.blueGrey,
                            ),
                            onChanged: (String? newValue) {
                              setState(() {
                                dropdownValue = newValue!;
                              });
                            },
                            items: <String>[
                              'Not seen yet',
                              'Under Review',
                              'Follow Up'
                            ].map<DropdownMenuItem<String>>((String value) {
                              return DropdownMenuItem<String>(
                                value: value,
                                child: Text(value),
                              );
                            }).toList(),
                          ),
                        ),
                      ],
                    ),
                    SizedBox(
                      height: 4.h,
                    ),
                    GestureDetector(
                      onTap: () => setState(() {
                        _launched = _launchInBrowser(widget.data["Image URL"]);
                      }),
                      child: Text(
                        "Click here to open media in browser",
                        style: TextStyle(
                          color: Colors.blue,
                          fontSize: 12.sp,
                        ),
                      ),
                    ),
                    SizedBox(
                      height: 2.h,
                    ),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceAround,
                      children: [
                        Container(
                          width: 80.w,
                          child: TextFormField(
                            decoration: authTextFieldDecoration.copyWith(
                              labelText: "Remark",
                              hintText: "Enter your remark",
                            ),
                            maxLines: 5,
                            controller: remarkController,
                            keyboardType: TextInputType.name,
                            onChanged: (val) {
                              setState(() {
                                if (val.isNotEmpty) {
                                  color = Colors.green;
                                } else {
                                  color = Colors.grey;
                                }
                              });
                            },
                          ),
                        ),
                        CircleAvatar(
                          backgroundColor: color,
                          child: IconButton(
                              onPressed: pushRemark,
                              icon: Icon(Icons.check, color: Colors.white)),
                        )
                      ],
                    ),
                    SizedBox(
                      height: 2.h,
                    ),
                    Row(
                      children: [
                        Align(
                          alignment: Alignment.center,
                          child: RoundedButton1(
                            color: Color(0xFF004AAD),
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
                                                  color: Colors.black),
                                            ),
                                            onPressed: () {
                                              Navigator.of(context).pop();
                                            },
                                          ),
                                          TextButton(
                                            child: const Text(
                                              "Yes",
                                              style: TextStyle(
                                                  color: Colors.green),
                                            ),
                                            onPressed: () {
                                              updateField(widget.data.id,
                                                  'finalStatus', 'inactive');
                                              Navigator.of(context).pop();
                                              Navigator.of(context).pop();
                                            },
                                          )
                                        ]);
                                  });
                            },
                            text: "Done",
                          ),
                        ),
                        SizedBox(
                          width: 2.w,
                        ),
                        Align(
                          alignment: Alignment.center,
                          child: RoundedButton1(
                            color: Color(0xFF004AAD),
                            onPressed: () {
                              final snackBar = new SnackBar(
                                  content: new Text(
                                      "The case has been escalated and will be given higher priority"),
                                  backgroundColor: Colors.blue);
                              ScaffoldMessenger.of(context)
                                  .showSnackBar(snackBar);
                              Navigator.pop(context);
                            },
                            text: "Escalate Issue",
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            ),
          ),
          // Padding(
          //   padding: EdgeInsets.symmetric(horizontal: 5.w),
          //   child: Container(
          //     height: 35.h,
          //     decoration: BoxDecoration(color: Colors.grey[850], boxShadow: [
          //       BoxShadow(
          //         color: Colors.blue,
          //         offset: Offset(15, 15),
          //       )
          //     ]),
          //     child: Padding(
          //       padding: EdgeInsets.symmetric(horizontal: 5.w),
          //       child: Column(
          //         crossAxisAlignment: CrossAxisAlignment.start,
          //         children: [
          //           SizedBox(
          //             height: 2.h,
          //           ),
          //           Text(
          //             "Issue description:",
          //             style: TextStyle(
          //                 fontSize: 14.sp,
          //                 fontWeight: FontWeight.bold,
          //                 color: Colors.white),
          //           ),
          //           Text(
          //             widget.data["Image Description"],
          //             style: TextStyle(fontSize: 14.sp, color: Colors.white),
          //           ),
          //           SizedBox(
          //             height: 4.h,
          //           ),
          //           Text(
          //             "Address:",
          //             style: TextStyle(
          //                 fontSize: 14.sp,
          //                 fontWeight: FontWeight.bold,
          //                 color: Colors.white),
          //           ),
          //           Text(
          //             "Near water tank, Mahanagar, 240006",
          //             style: TextStyle(fontSize: 12.sp, color: Colors.white),
          //           ),
          //           SizedBox(
          //             height: 4.h,
          //           ),
          //           Text(
          //             "Phone number:",
          //             style: TextStyle(
          //                 fontSize: 14.sp,
          //                 fontWeight: FontWeight.bold,
          //                 color: Colors.white),
          //           ),
          //           Text(
          //             "+919876509876",
          //             style: TextStyle(color: Colors.white),
          //           ),
          //         ],
          //       ),
          //     ),
          //   ),
          // ),
        ],
      ),
    );
  }
}
