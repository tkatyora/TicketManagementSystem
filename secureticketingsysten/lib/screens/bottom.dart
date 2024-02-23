import 'package:fluentui_icons/fluentui_icons.dart';
import 'package:flutter/material.dart';
import 'package:secureticketingsysten/screens/home.dart';
import 'package:secureticketingsysten/screens/scan.dart';
import 'package:secureticketingsysten/screens/settings.dart';
import 'package:secureticketingsysten/screens/tickert.dart';

class BottomBar extends StatefulWidget {
  const BottomBar({super.key});

  @override
  State<BottomBar> createState() => _BottomBarState();
}

class _BottomBarState extends State<BottomBar> {
  int _selectedIndex = 0;
  static final List<Widget> _widgetsOPtion = <Widget>[
    HomeScreen(),
    ScanScreen(),
    TickertScreen(),
    SettingsSCreen(),
  ];

  void _clickedItem(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Secure Ticketing System'),
      ),
      body: Center(
        child: _widgetsOPtion[_selectedIndex],
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _selectedIndex,
        onTap: _clickedItem,
        elevation: 10,
        showSelectedLabels: true,
        showUnselectedLabels: true,
        selectedItemColor: Colors.purple,
        unselectedItemColor: Colors.blueGrey,
        type: BottomNavigationBarType.fixed,
        items: <BottomNavigationBarItem>[
          // Add items for the bottom navigation bar
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'Home',
          ),
          BottomNavigationBarItem(
            icon: Icon(FluentSystemIcons.ic_fluent_qr_code_regular),
            activeIcon: Icon(FluentSystemIcons.ic_fluent_qr_code_filled),
            label: 'Scan Ticket',
          ),
          BottomNavigationBarItem(
            icon: Icon(FluentSystemIcons.ic_fluent_ticket_regular),
            activeIcon: Icon(FluentSystemIcons
                .ic_fluent_ticket_filled), // Using confirmation_number icon for ticket management
            label: 'Tickets',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.settings),
            label: 'Settings',
          ),
        ],
      ),
    );
  }
}
