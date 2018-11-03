import { Component, OnInit, Output, EventEmitter, Input } from '@angular/core';
import { LectureService } from '../../core/lecture.service';
import { Observable } from 'rxjs';
import {
  filter,
  debounceTime,
  distinctUntilChanged,
  switchMap
} from 'rxjs/operators';

@Component({
  selector: 'course-search',
  templateUrl: './course-search.component.html',
  styleUrls: ['./course-search.component.css']
})
export class CourseSearchComponent implements OnInit {
  @Input() pending: boolean;
  @Output() _search = new EventEmitter();
  name: string = null;
  grade: string = null;
  area: string = null;
  credit: number = null;
  department: any;
  type: string = null;
  lecturer: string = null;
  search;
  formatter = ({ name }) => name;

  constructor(private lecture: LectureService) {}

  ngOnInit() {
    this.search = (text$: Observable<string>) =>
      text$.pipe(
        filter((text: string) => text && text.length > 1),
        debounceTime(10),
        distinctUntilChanged(),
        switchMap((text: string) => this.lecture.searchDepartment(text))
      );
  }

  searchResult() {
    const payload = {
      name: this.name,
      grade: this.grade,
      area: this.area,
      creditTotal: this.credit,
      department: this.department && this.department.name,
      type: this.type,
      lecturer: this.lecturer
    };
    this._search.emit(payload);
  }

  reset() {
    this.name = null;
    this.grade = null;
    this.area = null;
    this.credit = null;
    this.department = null;
    this.type = null;
  }
}
