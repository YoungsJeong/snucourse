import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'course-list',
  templateUrl: './course-list.component.html',
  styleUrls: ['./course-list.component.css']
})
export class CourseListComponent implements OnInit {
  @Input() courses: any[];
  currentIndex = 0;
  constructor() {}

  ngOnInit() {}

  onClick(index: number) {
    this.currentIndex = index;
  }
}
