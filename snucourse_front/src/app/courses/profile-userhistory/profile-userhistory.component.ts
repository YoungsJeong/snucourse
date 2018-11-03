import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../core/auth.service';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'profile-userhistory',
  templateUrl: './profile-userhistory.component.html',
  styleUrls: ['./profile-userhistory.component.css']
})
export class ProfileUserhistoryComponent implements OnInit {
  constructor(public auth: AuthService, private modal: NgbModal) {}

  ngOnInit() {}

  openModal(content) {
    this.modal.open(content, { size: 'lg' });
  }
}
