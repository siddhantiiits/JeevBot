import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:nandi/screens/new_user/single_animal_boarders.dart';
import 'package:nandi/screens/new_user/single_animal_ngo.dart';
import 'package:sizer/sizer.dart';

import '../../animal_card.dart';
import '../../auth/login.dart';
import '../disease_reporting/single_animal_diseaseReporting.dart';

class NewProfile extends StatefulWidget {
  const NewProfile({Key? key, required this.uid}) : super(key: key);
  final String? uid;
  @override
  _NewProfileState createState() => _NewProfileState();
}

class _NewProfileState extends State<NewProfile> {
  String name = '';
  String role = '';
  void getData() async {
    var _data = await FirebaseFirestore.instance
        .collection("Users")
        .doc(widget.uid)
        .get();
    setState(() {
      name = _data.get('first-name');
      role = _data.get('role');
    });
  }

  @override
  void initState() {
    getData();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Welcome ${name}".toUpperCase()),
        actions: [
          Container(
              margin: EdgeInsets.only(right: 2.w),
              child: GestureDetector(
                  onTap: () async {
                    await FirebaseAuth.instance.signOut();
                    Navigator.pushReplacement(context,
                        MaterialPageRoute(builder: (context) => LogInPage()));
                  },
                  child: Icon(Icons.login))),
        ],
      ),
      body: Center(
        child: role == ""
            ? CircularProgressIndicator()
            : Column(
                children: [
                  SizedBox(
                    height: 5.h,
                  ),
                  CircleAvatar(
                    child: Image.asset("assets/images/nandi-logo.png"),
                    radius: 100,
                  ),
                  SizedBox(
                    height: 7.h,
                  ),
                  Text(
                    "You have 1 pending requests",
                    style: TextStyle(fontSize: 14.sp),
                  ),
                  SizedBox(
                    height: 1.5.h,
                  ),
                  role == "Boarders"
                      ? Column(
                          children: [
                            AnimalCard3(
                                imageName:
                                    "https://rr-europe.oie.int/wp-content/uploads/2020/01/fmd-cow.png",
                                number: "+91 827655331",
                                imageUrl: "Shivering, Sore Feet and Lips.",
                                data: {
                                  "address": "Dhaurera, Bareilly, 243006 (UP)",
                                  "Image URL":
                                      "https://rr-europe.oie.int/wp-content/uploads/2020/01/fmd-cow.png",
                                  "Name": "vansh",
                                  "Symptoms": "Shivering, Sore Feet and Lips.",
                                  "Image Description":
                                      "Shivering, Sore Feet and Lips.",
                                  "User Phone Number": "+91 827655331",
                                  "detected_disease": "FMD",
                                  "pincode": "243006",
                                  "status": "Not seen yet",
                                  "id": "1234567892"
                                }),
                            AnimalCard3(
                                imageName:
                                    "https://i2.wp.com/www.emeraldvet.com/wp-content/uploads/2012/01/26583.jpg.scaled1000.jpg?fit=800%2C600&ssl=1",
                                number: "+91 827655331",
                                imageUrl: "Bloody Diarrhoea, Fever, Lethargy",
                                data: {
                                  "address": "SCruz, Mumbai, 400047 (MH)",
                                  "Image URL":
                                      "https://i2.wp.com/www.emeraldvet.com/wp-content/uploads/2012/01/26583.jpg.scaled1000.jpg?fit=800%2C600&ssl=1",
                                  "Name": "vansh",
                                  "Symptoms":
                                      "Bloody Diarrhoea, Fever, Lethargy",
                                  "Image Description":
                                      "Shivering, Sore Feet and Lips.",
                                  "User Phone Number": "+91 827655331",
                                  "detected_disease": "Canine Parvo-virus",
                                  "pincode": "400047",
                                  "status": "Not seen yet",
                                  "id": "12345678912"
                                }),
                          ],
                        )
                      : Column(
                          children: [
                            AnimalCard4(
                                imageName:
                                    "https://allaboutbelgaum.com/wp-content/uploads/2020/12/bullock-cart-cane-768x311.jpeg",
                                number: " +91 786555331",
                                imageUrl: "Bulls with Excess Draught Load",
                                data: {
                                  "address": "Asawarpur, Sonipat, 131021 (HR)",
                                  "Image URL":
                                      "https://allaboutbelgaum.com/wp-content/uploads/2020/12/bullock-cart-cane-768x311.jpeg",
                                  "Name": "vansh",
                                  "Symptoms": "Bulls with Excess Draught Load",
                                  "Image Description":
                                      "Bulls with Excess Draught Load",
                                  "User Phone Number": " +91 786555331",
                                  "detected_disease": "FMD",
                                  "pincode": "131021",
                                  "status": "Not seen yet",
                                  "id": "123456789"
                                }),
                            AnimalCard4(
                                imageName:
                                    "https://s3.ap-southeast-1.amazonaws.com/images.asianage.com/images/aa-Cover-2ufe01efbqeqkp7696q7hoehe2-20170313024404.jpeg",
                                number: "+91 827655331",
                                imageUrl: "Dogs harmed with toxic colours",
                                data: {
                                  "address": "Jaipur, Rajasthan, 302004 (RJ)",
                                  "Image URL":
                                      "https://s3.ap-southeast-1.amazonaws.com/images.asianage.com/images/aa-Cover-2ufe01efbqeqkp7696q7hoehe2-20170313024404.jpeg",
                                  "Name": "vansh",
                                  "Symptoms": " Dogs harmed with toxic colours",
                                  "Image Description":
                                      "Dogs harmed with toxic colours.",
                                  "User Phone Number": "+91 756342886",
                                  "detected_disease": "Canine Parvo-virus",
                                  "pincode": "302004",
                                  "status": "Not seen yet",
                                  "id": "1234567891"
                                }),
                          ],
                        ),
                ],
              ),
      ),
    );
  }
}

class AnimalCard3 extends StatelessWidget {
  final String imageName;
  final String imageUrl;
  final String number;
  final data;
  AnimalCard3(
      {required this.imageName,
      required this.imageUrl,
      required this.number,
      required this.data});
  @override
  Widget build(BuildContext context) {
    return Container(
      child: GestureDetector(
        onTap: () {
          Navigator.push(
              context,
              MaterialPageRoute(
                  builder: (context) => SingleAnimalPage2(data: data)));
        },
        child: Padding(
          padding: EdgeInsets.only(top: 0.2.h),
          child: Card(
            child: Padding(
              padding: EdgeInsets.symmetric(vertical: 0.5.h),
              child: ListTile(
                leading: Hero(
                  tag: "${data["id"]}",
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(50),
                    child: Image.network(
                      imageName,
                      width: 60,
                      height: 100,
                      fit: BoxFit.cover,
                    ),
                  ),
                ),
                title: Text(imageUrl),
                subtitle: Text(number),
              ),
            ),
          ),
        ),
      ),
    );
  }
}

class AnimalCard4 extends StatelessWidget {
  final String imageName;
  final String imageUrl;
  final String number;
  final data;
  AnimalCard4(
      {required this.imageName,
      required this.imageUrl,
      required this.number,
      required this.data});
  @override
  Widget build(BuildContext context) {
    return Container(
      child: GestureDetector(
        onTap: () {
          Navigator.push(
              context,
              MaterialPageRoute(
                  builder: (context) => SingleAnimalPage3(data: data)));
        },
        child: Padding(
          padding: EdgeInsets.only(top: 0.2.h),
          child: Card(
            child: Padding(
              padding: EdgeInsets.symmetric(vertical: 0.5.h),
              child: ListTile(
                leading: Hero(
                  tag: "${data["id"]}",
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(50),
                    child: Image.network(
                      imageName,
                      width: 60,
                      height: 100,
                      fit: BoxFit.cover,
                    ),
                  ),
                ),
                title: Text(imageUrl),
                subtitle: Text(number),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
