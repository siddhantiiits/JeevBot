import 'package:firebase/firebase.dart';
import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart' as auth_service;
import 'package:nandi_portal/animal_welfare.dart';
import 'package:splash_screen_view/SplashScreenView.dart';
import 'package:firebase_core/firebase_core.dart' as core;
import 'package:firebase/firebase.dart' as WebFirebase;

import 'email_login.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await core.Firebase.initializeApp(
      options: const core.FirebaseOptions(
          apiKey: "AIzaSyC014jfAbtT-sxxvBas1eppNzNlMuLo53M",
          appId: "1:1041001071112:web:d9a01fd024f12d8f9007bd",
          messagingSenderId: "1041001071112",
          projectId: "nandi-2adc2"));
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
        future: core.Firebase.initializeApp(),
        builder: (context, snapshot) {
          if (snapshot.hasError) {
            print('has error');
            print(snapshot.error.toString());
            return Center(child: Container(child: RefreshProgressIndicator()));
          }

          // Once complete, show your application
          if (snapshot.connectionState == ConnectionState.done) {
            return MaterialApp(
              debugShowCheckedModeBanner: false,
              title: 'Nandi',
              theme: ThemeData(
                primarySwatch: Colors.cyan,
              ),
              home: IntroScreen(),
            );
          }

          // Otherwise, show something whilst waiting for initialization to complete
          return CircularProgressIndicator();
        });
  }
}

class IntroScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    auth_service.FirebaseAuth auth = auth_service.FirebaseAuth.instance;
    print("build intro-");
    return SplashScreenView(
      navigateRoute: auth.currentUser != null
          ? (animalWelfare(user: auth.currentUser!))
          : EmailLogIn(),
      duration: 30, //3000
      text: 'Welcome To NANDI!!',
      textType: TextType.TyperAnimatedText,
      textStyle: const TextStyle(fontWeight: FontWeight.bold, fontSize: 20.0),
      colors: [
        Colors.blue.shade900,
        Colors.yellow,
        Colors.red,
        Colors.lightBlue.shade900,
      ],
      backgroundColor: Colors.white,
      // onClick: () => print("flutter"),
      // loaderColor: Colors.red,
    );
  }
}
