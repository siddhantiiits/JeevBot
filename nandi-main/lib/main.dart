import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'auth/login.dart';
import 'package:sizer/sizer.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Sizer(
      builder: (context, orientation, deviceType) {
        return MaterialApp(
          themeMode: ThemeMode.dark,
          theme: ThemeData(
            fontFamily: 'WorkSans',
            primarySwatch: Colors.indigo,
          ),
          // darkTheme: ThemeData.dark(),
          debugShowCheckedModeBanner: false,
          home: LogInPage(),
        );
      },
    );
  }
}
