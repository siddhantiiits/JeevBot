import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:nandi/utils/RoundedButton.dart';
import 'package:nandi/utils/RoundedButton1.dart';
import 'package:sizer/sizer.dart';
import 'package:url_launcher/url_launcher.dart';

import '../../constants.dart';

class SingleAnimalPage2 extends StatefulWidget {
  final data;
  SingleAnimalPage2({required this.data});

  @override
  _SingleAnimalPage2State createState() => _SingleAnimalPage2State();
}

class _SingleAnimalPage2State extends State<SingleAnimalPage2> {
  late TextEditingController remarkController;
  Future<void>? _launched;

  Future<void> updateField(String docID, String fieldName, String fieldValue) {
    return FirebaseFirestore.instance
        .collection('AnimalWelfare')
        .doc(docID)
        .update({fieldName: fieldValue})
        .then((value) => print("User Updated"))
        .catchError((error) => print("Failed to update user: $error"));
  }

  void pushRemark() async {
    if (remarkController.value.text.isNotEmpty) {
      await FirebaseFirestore.instance
          .collection('Disease Reporting')
          .doc(widget.data.id)
          .update({'detected_disease': remarkController.value.text});
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
    remarkController =
        TextEditingController(text: widget.data['detected_disease']);
    super.initState();
  }

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

  Color color = Colors.grey;
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
              tag: widget.data["id"],
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
                        widget.data["Symptoms"].toString().toUpperCase(),
                        style: TextStyle(
                          fontSize: 20.sp,
                          fontWeight: FontWeight.bold,
                        ),
                        textAlign: TextAlign.center,
                      ),
                    ),
                    SizedBox(
                      height: 1.h,
                    ),
                    Container(
                      child: Text(
                        "Auto-detected Disease: ${widget.data["detected_disease"]} ",
                        style: TextStyle(fontSize: 12.sp, color: Colors.red),
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
                      height: 1.h,
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
                        Text(
                          "Pincode: ${widget.data["pincode"]}",
                          style: TextStyle(fontSize: 13.sp),
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
                              labelText: "Disease",
                              hintText: "Enter suggested disease",
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
                              final snackBar = new SnackBar(
                                  content: new Text(
                                      "The case has been marked as done"),
                                  backgroundColor: Colors.blue);
                              ScaffoldMessenger.of(context)
                                  .showSnackBar(snackBar);
                              Navigator.pop(context);
                            },
                            text: "Redirect",
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
                            text: "Resolved",
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
