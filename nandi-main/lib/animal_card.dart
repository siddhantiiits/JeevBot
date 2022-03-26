import 'package:flutter/material.dart';
import 'package:nandi/screens/animal_welfare/single_animal_animalWelfare.dart';
import 'package:sizer/sizer.dart';

class AnimalCard extends StatelessWidget {
  final String imageName;
  final String imageUrl;
  final String number;
  var data;

  AnimalCard(
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
                  builder: (context) => SingleAnimalPage(data: data)));
        },
        child: Padding(
          padding: EdgeInsets.only(top: 0.2.h),
          child: Card(
            child: Padding(
              padding: EdgeInsets.symmetric(vertical: 0.5.h),
              child: ListTile(
                leading: Hero(
                  tag: "$imageName",
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
