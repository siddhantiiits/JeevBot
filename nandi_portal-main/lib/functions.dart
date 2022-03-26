import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:nandi_portal/animal_welfare.dart';
import 'package:nandi_portal/disease_reporting.dart';

drawers(BuildContext context, int i, User user) {
  return Column(
    children: <Widget>[
      Expanded(
        child: Column(
          children: [
            Column(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                Image.asset(
                  "assets/images/nandi-logo.png",
                  // color: Colors.white,
                ),
                // Image.network(
                //   'https://firebasestorage.googleapis.com/v0/b/nandi-2adc2.appspot.com/o/logo%2Fnandi-logo.png?alt=media&token=90930fa5-1f67-4971-aaa1-7773af77e834',
                //   loadingBuilder: (BuildContext context, Widget child,
                //       ImageChunkEvent? loadingProgress) {
                //     if (loadingProgress == null) return child;
                //     return Center(
                //       child: CircularProgressIndicator(
                //         value: loadingProgress.expectedTotalBytes != null
                //             ? loadingProgress.cumulativeBytesLoaded /
                //                 loadingProgress.expectedTotalBytes!
                //             : null,
                //       ),
                //     );
                //   },
                // ),
                // NetworkImage('https://firebasestorage.googleapis.com/v0/b/nandi-2adc2.appspot.com/o/logo%2Fnandi-logo.png?alt=media&token=90930fa5-1f67-4971-aaa1-7773af77e834'),
                // Text(
                //   'Nandi!',
                //   textScaleFactor: 2,
                // ),
                Text('Welcome ' + user.displayName!),
                Padding(
                  padding: const EdgeInsets.fromLTRB(30, 10, 30, 0),
                  child: Divider(),
                ),
                ListTile(
                  selected: (i == 1) ? true : false,
                  leading: const Icon(Icons.pets),
                  title: const Text('Animal Welfare'),
                  onTap: () => Navigator.of(context).pushReplacement(
                      MaterialPageRoute(
                          builder: (context) => animalWelfare(user: user))),
                ),
                ListTile(
                  selected: (i == 2) ? true : false,
                  leading: const Icon(Icons.medical_services),
                  title: const Text('Disease Reporting'),
                  onTap: () => Navigator.of(context).pushReplacement(
                      MaterialPageRoute(
                          builder: (context) => DiseaseReporting(user: user))),
                ),
              ],
            ),
          ],
        ),
      ),
    ],
  );
}
