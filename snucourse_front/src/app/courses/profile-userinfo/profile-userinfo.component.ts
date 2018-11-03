import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../core/auth.service';

@Component({
  selector: 'profile-userinfo',
  templateUrl: './profile-userinfo.component.html',
  styleUrls: ['./profile-userinfo.component.css']
})
export class ProfileUserinfoComponent implements OnInit {
  constructor(public auth: AuthService) {}

  ngOnInit() {}
}
