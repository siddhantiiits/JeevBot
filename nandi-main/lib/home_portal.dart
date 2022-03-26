import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:nandi/auth/login.dart';
import 'package:nandi/screens/animal_welfare/animal_welfare.dart';
import 'package:nandi/screens/animal_welfare/single_animal_animalWelfare.dart';
import 'package:sizer/sizer.dart';

import 'screens/disease_reporting/disease_reporting.dart';

class PortalHome extends StatefulWidget {
  const PortalHome({Key? key}) : super(key: key);

  @override
  _PortalHomeState createState() => _PortalHomeState();
}

class _PortalHomeState extends State<PortalHome> {
  bool isSelected = true;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.indigo.shade100,
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: [
            DrawerHeader(
              child: Image.asset('assets/images/nandi-logo.png'),
            ),
            Padding(
              padding: EdgeInsets.only(left: 10.w, right: 10.w),
              child: Divider(
                color: Colors.grey,
                thickness: 2.0,
              ),
            ),
            ListTile(
              selected: isSelected,
              title: const Text('Animal Welfare'),
              onTap: () {
                setState(() {
                  isSelected = true;
                });
                Navigator.pop(context);
              },
              leading: Icon(Icons.pets),
            ),
            ListTile(
              selected: !isSelected,
              title: const Text('Disease Reporting'),
              onTap: () {
                setState(() {
                  isSelected = false;
                });
                Navigator.pop(context);
              },
              leading: Icon(Icons.medical_services_outlined),
            ),
          ],
        ),
      ),
      appBar: AppBar(
        title: Text(
          "${isSelected ? "Animal Abuse " : "Disease Reporting "}Portal",
          style: TextStyle(fontSize: 14.sp),
        ),
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
      body: isSelected ? AnimalWelfare() : DiseaseReporting(),
    );
  }
}
