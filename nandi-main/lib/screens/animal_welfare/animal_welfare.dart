import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:nandi/screens/animal_welfare/single_animal_animalWelfare.dart';
import 'package:sizer/sizer.dart';

import '../../animal_card.dart';

class AnimalWelfare extends StatefulWidget {
  const AnimalWelfare({Key? key}) : super(key: key);

  @override
  _AnimalWelfareState createState() => _AnimalWelfareState();
}

class _AnimalWelfareState extends State<AnimalWelfare> {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: StreamBuilder(
        stream: FirebaseFirestore.instance
            .collection('AnimalWelfare')
            .where('finalStatus', isEqualTo: 'active')
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
                return AnimalCard(
                  number: document["User Phone Number"],
                  imageUrl: document["Image Description"],
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
