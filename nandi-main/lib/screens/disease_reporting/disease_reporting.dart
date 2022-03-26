import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:sizer/sizer.dart';

import 'single_animal_diseaseReporting.dart';

class DiseaseReporting extends StatefulWidget {
  const DiseaseReporting({Key? key}) : super(key: key);

  @override
  _DiseaseReportingState createState() => _DiseaseReportingState();
}

class _DiseaseReportingState extends State<DiseaseReporting> {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: StreamBuilder(
        stream: FirebaseFirestore.instance
            .collection('Disease Reporting')
            .snapshots(),
        builder: (BuildContext context, AsyncSnapshot<dynamic> snapshot) {
          if (!snapshot.hasData) {
            return Center(
              child: CircularProgressIndicator(),
            );
          }
          return ListView(children: <Widget>[
            ...snapshot.data!.docs.map(
              (document) {
                print(document);
                return AnimalCard2(
                  number: document["User Phone Number"],
                  imageUrl: document["Symptoms"],
                  imageName: document["Image URL"],
                  data: document,
                );
              },
            ),
          ]);
        },
      ),
    );
  }
}

class AnimalCard2 extends StatelessWidget {
  final String imageName;
  final String imageUrl;
  final String number;
  final data;
  AnimalCard2(
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
                  builder: (context) => SingleAnimalPage1(data: data)));
        },
        child: Padding(
          padding: EdgeInsets.only(top: 0.2.h),
          child: Card(
            child: Padding(
              padding: EdgeInsets.symmetric(vertical: 0.5.h),
              child: ListTile(
                leading: Hero(
                  tag: "${data.id}",
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
